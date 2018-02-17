CREATE SCHEMA IF NOT EXISTS subscriptions AUTHORIZATION grp_crud;
COMMENT ON SCHEMA subscriptions IS 'eCommerce Data - online and phone based subscription products';

-- All Access
ALTER DEFAULT PRIVILEGES FOR ROLE grp_crud, superadmin IN SCHEMA subscriptions GRANT ALL ON TABLES TO grp_crud;
ALTER DEFAULT PRIVILEGES FOR ROLE grp_crud, superadmin IN SCHEMA subscriptions GRANT ALL ON FUNCTIONS TO grp_crud;
ALTER DEFAULT PRIVILEGES FOR ROLE grp_crud, superadmin IN SCHEMA subscriptions GRANT ALL ON SEQUENCES TO grp_crud;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA subscriptions TO grp_crud;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA subscriptions TO grp_crud;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA subscriptions TO grp_crud;

-- Read Access
ALTER DEFAULT PRIVILEGES FOR ROLE grp_crud, superadmin IN SCHEMA subscriptions GRANT SELECT ON TABLES TO grp_read;
GRANT SELECT ON ALL TABLES IN SCHEMA subscriptions TO grp_read;

-- Table creation
BEGIN;
    SET ROLE grp_crud;
    SET search_path = subscriptions;


    -- Customer table to capture each customer and their contact information (dimension table)
    CREATE TABLE customer (
        id BIGINT NOT NULL PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        street_address TEXT,
        state TEXT,
        zip_code TEXT
    );
    CREATE UNIQUE INDEX customerid_idx ON customer (id);
    COMMENT ON TABLE customer IS 'Customer contact information';


    -- Product table to capture each prodct and its cost (dimension table)
    CREATE TABLE product (
        id BIGINT NOT NULL PRIMARY KEY,
        product_name VARCHAR(100),
        cost DECIMAL(12,2)
    );
    CREATE UNIQUE INDEX productid_idx ON product (id);
    COMMENT ON TABLE product IS 'Products for purchase';


    -- Sales table to capture transactions over time as they are processed (fact table)
    CREATE TYPE status AS ENUM ('new', 'canceled');
    CREATE TABLE sales (
        id SERIAL,
        customer_id BIGINT NOT NULL REFERENCES customer(id),
        product_id BIGINT NOT NULL REFERENCES product(id),
        purchase_status status,
        transaction_date TIMESTAMPTZ NOT NULL,
        CONSTRAINT transaction UNIQUE (customer_id, product_id, purchase_status, transaction_date)
    );
    CREATE UNIQUE INDEX customerid_productid_idx ON sales (customer_id, product_id);
    COMMENT ON TABLE sales IS 'Sales records';


END;
