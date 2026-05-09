📦 Kho Mẹ có git
├── Public/ 
└── Private(có git riêng)/

- Public + Private đều sync lên Kho Mẹ
- Riêng Private tiếp tục sync sang Kho Con

📦 Kho Con
└── Private/

Logic:

Kho Mẹ = tổng hợp toàn bộ

Kho Con = kế thừa một phần dữ liệu từ Kho Mẹ

Một nguồn dữ liệu có thể thuộc nhiều kho mà không cần duplicate quản lý

cái nào mà muốn công khai thì người dùng sẽ chuyển file vô Folder Public rồi push. để tách biệt ra chứ không có để chung rồi phân loại hiểu không