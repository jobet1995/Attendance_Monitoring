CREATE TABLE "User" (
  "id" int PRIMARY KEY,
  "username" varchar(100) NOT NULL,
  "email" varchar(255) NOT NULL,
  "password" varchar(255) NOT NULL,
  "first_name" varchar(100),
  "last_name" varchar(100),
  "role" varchar(50)
);

CREATE TABLE "Profile" (
  "id" int PRIMARY KEY,
  "name" varchar(100) NOT NULL,
  "user_id" int
);

CREATE TABLE "Product" (
  "id" int PRIMARY KEY,
  "name" varchar(255) NOT NULL,
  "description" text,
  "price" decimal(10,2),
  "stock" int
);

CREATE TABLE "Supplier" (
  "id" int PRIMARY KEY,
  "name" varchar(255) NOT NULL,
  "contact_info" text
);

CREATE TABLE "ProductSupplier" (
  "id" int PRIMARY KEY,
  "product_id" int,
  "supplier_id" int
);

CREATE TABLE "Order" (
  "id" int PRIMARY KEY,
  "order_date" datetime,
  "user_id" int
);

CREATE TABLE "OrderDetail" (
  "id" int PRIMARY KEY,
  "order_id" int,
  "product_id" int,
  "quantity" int,
  "unit_price" decimal(10,2)
);

CREATE TABLE "Customer" (
  "id" int PRIMARY KEY,
  "customer_name" varchar(255) NOT NULL,
  "contact_name" varchar(255),
  "address" text,
  "city" varchar(100),
  "postal_code" varchar(20),
  "country" varchar(100),
  "phone" varchar(50)
);

CREATE TABLE "CustomerOrder" (
  "id" int PRIMARY KEY,
  "customer_id" int,
  "order_date" date,
  "status" varchar(50)
);

CREATE TABLE "CustomerOrderDetail" (
  "id" int PRIMARY KEY,
  "customer_order_id" int,
  "product_id" int,
  "quantity" int,
  "unit_price" decimal(10,2)
);

CREATE TABLE "Shipment" (
  "id" int PRIMARY KEY,
  "shipment_date" date,
  "carrier" varchar(255),
  "tracking_number" varchar(255),
  "status" varchar(50)
);

CREATE TABLE "ShipmentDetail" (
  "id" int PRIMARY KEY,
  "shipment_id" int,
  "order_id" int,
  "customer_order_id" int,
  "product_id" int,
  "quantity" int
);

CREATE TABLE "StockAdjustment" (
  "id" int PRIMARY KEY,
  "product_id" int,
  "warehouse_id" int,
  "adjustment_date" date,
  "quantity" int,
  "reason" varchar(255)
);

CREATE TABLE "InventoryTransaction" (
  "id" int PRIMARY KEY,
  "product_id" int,
  "warehouse_id" int,
  "quantity" int,
  "transaction_type" varchar(50),
  "transaction_date" datetime
);

CREATE TABLE "Warehouse" (
  "id" int PRIMARY KEY,
  "warehouse_name" varchar(255) NOT NULL,
  "location" varchar(255) NOT NULL,
  "created_at" datetime
);

CREATE TABLE "Task" (
  "id" int PRIMARY KEY,
  "title" varchar(255) NOT NULL,
  "description" text,
  "due_date" date,
  "completed" boolean,
  "assigned_to" int
);

CREATE TABLE "Event" (
  "id" int PRIMARY KEY,
  "name" varchar(255) NOT NULL,
  "description" text,
  "start_time" datetime,
  "end_time" datetime,
  "location" varchar(255)
);

CREATE INDEX "product_supplier_idx" ON "ProductSupplier" ("product_id", "supplier_id");

ALTER TABLE "Profile" ADD FOREIGN KEY ("user_id") REFERENCES "User" ("id");

ALTER TABLE "ProductSupplier" ADD FOREIGN KEY ("product_id") REFERENCES "Product" ("id");

ALTER TABLE "ProductSupplier" ADD FOREIGN KEY ("supplier_id") REFERENCES "Supplier" ("id");

ALTER TABLE "Order" ADD FOREIGN KEY ("user_id") REFERENCES "User" ("id");

ALTER TABLE "OrderDetail" ADD FOREIGN KEY ("order_id") REFERENCES "Order" ("id");

ALTER TABLE "OrderDetail" ADD FOREIGN KEY ("product_id") REFERENCES "Product" ("id");

ALTER TABLE "CustomerOrder" ADD FOREIGN KEY ("customer_id") REFERENCES "Customer" ("id");

ALTER TABLE "CustomerOrderDetail" ADD FOREIGN KEY ("customer_order_id") REFERENCES "CustomerOrder" ("id");

ALTER TABLE "CustomerOrderDetail" ADD FOREIGN KEY ("product_id") REFERENCES "Product" ("id");

ALTER TABLE "ShipmentDetail" ADD FOREIGN KEY ("shipment_id") REFERENCES "Shipment" ("id");

ALTER TABLE "ShipmentDetail" ADD FOREIGN KEY ("order_id") REFERENCES "Order" ("id");

ALTER TABLE "ShipmentDetail" ADD FOREIGN KEY ("customer_order_id") REFERENCES "CustomerOrder" ("id");

ALTER TABLE "ShipmentDetail" ADD FOREIGN KEY ("product_id") REFERENCES "Product" ("id");

ALTER TABLE "StockAdjustment" ADD FOREIGN KEY ("product_id") REFERENCES "Product" ("id");

ALTER TABLE "StockAdjustment" ADD FOREIGN KEY ("warehouse_id") REFERENCES "Warehouse" ("id");

ALTER TABLE "InventoryTransaction" ADD FOREIGN KEY ("product_id") REFERENCES "Product" ("id");

ALTER TABLE "InventoryTransaction" ADD FOREIGN KEY ("warehouse_id") REFERENCES "Warehouse" ("id");

ALTER TABLE "Task" ADD FOREIGN KEY ("assigned_to") REFERENCES "User" ("id");
