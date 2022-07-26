# Crawl dữ liệu với python

### *Xin chào mọi người,*

Trong bài viết này, mình xin trình bày cách lấy dữ liệu trong một trang web với python.

## 1. Cài đặt các thư viện

Đầu tiên bạn cần phải cài sẵn thư viện sau về máy tính.

```bash
#Install requests để thực hiện gửi yêu cầu đến trang web cần data
pip install requests
```

Tiếp theo truy cập vào trang web bạn muốn lấy dữ liệu, ở đây mình lấy dữ liệu từ trang [https://goctruyentranhhay.com](https://goctruyentranhhay.com/danh-sach?type=NEW)

## 2. Lấy dữ liệu thô của trang web

Sử dụng **F12/Fn+F12** hoặc click chuột trái chọn **Inspect** (Kiểm tra) để mở cửa sổ Kiểm tra phần tử

Tại cửa sổ này, ta chọn đến **Network -> Fetch/XHR** rồi reload lại trang để gửi lại HTTP request (xem hình minh họa)

![image](https://user-images.githubusercontent.com/92797788/180935132-dae0552b-df8e-4aed-abc9-2a67794fbc35.png)

Tiếp theo ta double click vào **new?p=0**, sẽ mở ra một tab mới như hình bên dưới

![image](https://user-images.githubusercontent.com/92797788/180935558-d942b18c-0c90-4d8e-adf8-b42c17a898c2.png)

Nếu muốn dễ nhìn như hình bạn cần cài thêm một extension cho trình duyệt chrome [tại đây](https://chrome.google.com/webstore/detail/json-viewer-pro/eifflpmocdbdmepbjaopkkhbfmdgijcc)

## 3. Phân tích dữ liệu

Như hình trên, để lấy được dữ liệu tên truyện ta chỉ cần truy cập đến trường ***name*** trong ***result/data***

Để ý thêm tại đường link trang API chỉ cần thay đổi số sau **/new?p=** thì ta có dữ liệu trang tiếp theo. 

## 4. Tổng kết

Ý tưởng cơ bản là như vậy, bạn đọc hãy nghiên cứu code nhé <(^-^)>.

Bài viết còn rất lủng củng, mong mọi người thứ lỗi. ***Damn!!!Wibu is the best***


