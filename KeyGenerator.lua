local os_date = os.date("%Y-%m-%d") -- Lấy ngày hiện tại (VD: "2024-12-07")
local prefix = "HappyHub_"
local hash = "h1Df32UHO8932" -- Bạn có thể tự thay đổi hoặc băm thêm.

-- Tạo key:
local key = prefix .. os_date:gsub("-", "") .. "_" .. hash
return key
