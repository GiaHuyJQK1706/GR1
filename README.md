# Nghiên cứu tốt nghiệp 1

Tìm hiểu một trong các mô hình thiết kế phần mềm (MVC/MVT/MVP/MVVM), tìm hiểu 1 framework xây dựng hệ thống ứng dụng và làm 1 ứng dụng web app/mobile app đơn giản

## Mục Lục

  - [Công nghệ sử dụng](#công-nghệ-sử-dụng)
  - [Giới thiệu về công nghệ Django](#giới-thiệu-về-công-nghệ-django)
    - [Mô hình MVT trong Django](#mô-hình-mvt-trong-django)
    - [So sánh mô hình MVT và MVC](#so-sánh-mô-hình-mvt-và-mvc)
  - [Giới thiệu về công nghệ SQLite](#giới-thiệu-về-công-nghệ-sqlite)
    - [SQLite Là Gì?](#sqlite-là-gì)
      - [Ưu Điểm](#ưu-điểm)
      - [Nhược Điểm](#nhược-điểm)
    - [SQLite Trong Django](#sqlite-trong-django)
      - [So Sánh SQLite Với Các Hệ QTCSDL Khác](#so-sánh-sqlite-với-các-hệ-qtcddl-khác)
        - [So Sánh Với Các Hệ QTCSDL SQL Khác](#so-sánh-với-các-hệ-qtcddl-sql-khác)
        - [So Sánh Với Các Hệ QTCSDL NoSQL](#so-sánh-với-các-hệ-qtcddl-nosql)
      - [Kết Luận](#kết-luận)
  - [Cài đặt kho lưu trữ GR1](#cài-đặt-kho-lưu-trữ-gr1)

## Công nghệ sử dụng

- **Django**: Một framework web Python cao cấp, khuyến khích phát triển nhanh và thiết kế gọn gàng, thực dụng.
- **HTML/CSS/JS**: Các công nghệ tiêu chuẩn để xây dựng và thiết kế các trang web.
- **Bootstrap**: Một framework front-end phổ biến để phát triển các trang web responsive và ưu tiên thiết bị di động.
- **SQLite**: Một thư viện ngôn ngữ C cung cấp cơ sở dữ liệu nhẹ, lưu trữ trên đĩa.
- **Jinja2**: Một công cụ tạo mẫu cho Python.
- **jQuery**: Một thư viện JavaScript nhanh, nhỏ gọn và nhiều tính năng.


## Giới thiệu về công nghệ Django

Django là một framework web cấp cao được viết bằng Python, khuyến khích phát triển nhanh và thiết kế sạch sẽ, thực dụng. Được xây dựng bởi các nhà phát triển giàu kinh nghiệm, nó chăm sóc rất nhiều rắc rối của phát triển web, vì vậy bạn có thể tập trung vào việc viết ứng dụng của bạn mà không cần phải tốn nhiều công sức. Trong project Django có rất nhiều app con để dễ quản lý hơn

### Mô hình MVT trong Django

Django sử dụng mô hình MVT (Model-View-Template), là một biến thể của mô hình MVC (Model-View-Controller) phổ biến:

- **Model**: Quản lý dữ liệu và logic nghiệp vụ. Trong Django, các mô hình là các lớp Python thuần túy được định nghĩa trong `models.py`.
- **View**: Điều khiển luồng dữ liệu và hiển thị kết quả. Trong Django, các view là các hàm hoặc lớp trong `views.py` xử lý các yêu cầu HTTP và trả về các phản hồi HTTP.
- **Template**: Định nghĩa giao diện người dùng của ứng dụng. Trong Django, các template là các tệp HTML với các cú pháp đặc biệt cho phép chèn dữ liệu động từ các view.

Mỗi app con trong một project Django bắt buộc phải có 3 lớp **models**, **views**, **urls**. Mỗi project Django bắt buộc phải có ít nhất 1 app con

### So sánh mô hình MVT và MVC

- **MVC (Model-View-Controller)**:
  - **Model**: Quản lý dữ liệu và logic nghiệp vụ.
  - **View**: Hiển thị dữ liệu, định nghĩa giao diện người dùng.
  - **Controller**: Điều khiển luồng dữ liệu giữa Model và View.

- **MVT (Model-View-Template)**:
  - **Model**: Quản lý dữ liệu và logic nghiệp vụ.
  - **View**: Điều khiển luồng dữ liệu và hiển thị kết quả.
  - **Template**: Định nghĩa giao diện người dùng của ứng dụng.

Sự khác biệt chính giữa MVT và MVC là trong MVT, Django tự động xử lý phần "Controller" (chính là "View" trong Django) và kết nối giữa các Model và Template, giúp giảm bớt công việc cho lập trình viên. Điều này làm cho MVT trở nên dễ hiểu và dễ triển khai hơn so với MVC truyền thống.

Django cũng tích hợp sẵn nhiều tính năng mạnh mẽ như hệ thống quản lý người dùng, quản lý cơ sở dữ liệu, và nhiều hơn nữa, giúp bạn xây dựng ứng dụng web một cách nhanh chóng và hiệu quả.

## Giới thiệu về công nghệ SQLite

### SQLite Là Gì?

SQLite là một thư viện ngôn ngữ C cung cấp cơ sở dữ liệu nhẹ, lưu trữ trên đĩa. Không giống như hầu hết các hệ quản trị cơ sở dữ liệu SQL khác, SQLite không có quy trình máy chủ riêng biệt. Thư viện SQLite được liên kết trực tiếp vào chương trình ứng dụng, và dữ liệu được lưu trữ trong một tập tin đơn giản.

#### Ưu Điểm:

- **Nhẹ và Nhanh**: Thích hợp cho các ứng dụng nhỏ hoặc dùng để phát triển.
- **Không Cần Cấu Hình**: Dễ dàng thiết lập và bắt đầu sử dụng.
- **Tương Thích Đa Nền Tảng**: Chạy trên nhiều hệ điều hành.

#### Nhược Điểm:

- **Không Phù Hợp Với Ứng Dụng Lớn**: Không thích hợp cho các ứng dụng yêu cầu khả năng mở rộng cao.
- **Giới Hạn Tính Năng**: Thiếu một số tính năng mà các hệ QTCSDL lớn hơn cung cấp.

## SQLite Trong Django

Django hỗ trợ SQLite như là cơ sở dữ liệu mặc định. Dưới đây là cách cấu hình SQLite trong dự án Django:

1. Tạo dự án Django mới:
    ```bash
    django-admin startproject myproject
    ```

2. Cấu hình cơ sở dữ liệu trong tệp `settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```

3. Chạy lệnh để tạo cơ sở dữ liệu:
    ```bash
    python manage.py migrate
    ```

### So Sánh SQLite Với Các Hệ QTCSDL Khác

#### So Sánh Với Các Hệ QTCSDL SQL Khác

- **PostgreSQL**:
  - Ưu Điểm: Hỗ trợ tính năng phức tạp, mạnh mẽ và an toàn, khả năng mở rộng cao.
  - Nhược Điểm: Cần cấu hình và quản lý, nặng hơn SQLite.

- **MySQL**:
  - Ưu Điểm: Hiệu năng cao, phổ biến và được hỗ trợ rộng rãi.
  - Nhược Điểm: Cần cấu hình và quản lý, nặng hơn SQLite.

#### So Sánh Với Các Hệ QTCSDL NoSQL

- **MongoDB**:
  - Ưu Điểm: Linh hoạt với dữ liệu không có cấu trúc, dễ mở rộng.
  - Nhược Điểm: Không tuân theo chuẩn SQL, có thể phức tạp hơn khi quản lý các quan hệ dữ liệu.

- **Cassandra**:
  - Ưu Điểm: Khả năng mở rộng và chịu lỗi cao, phù hợp cho ứng dụng lớn.
  - Nhược Điểm: Không hỗ trợ mạnh mẽ cho các truy vấn phức tạp, phức tạp khi cài đặt và quản lý.

### Kết Luận

SQLite là một lựa chọn tuyệt vời cho các ứng dụng nhỏ và phát triển nhanh, nhưng không phù hợp cho các ứng dụng yêu cầu khả năng mở rộng và tính năng cao cấp.


## Cài đặt kho lưu trữ GR1

Để cài đặt và chạy ứng dụng web GR1, hãy làm theo các bước sau:

1. Clone repository về máy tính của bạn:
    ```bash
    git clone https://github.com/GiaHuyJQK1706/GR1.git
    ```

2. Điều hướng đến thư mục dự án:
    ```bash
    cd GR1
    ```

3. Cài đặt các dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Thực hiện các migration cơ sở dữ liệu:
    ```bash
    python manage.py migrate
    ```

5. Tạo tài khoản superuser (tài khoản quản trị) cho giao diện quản trị Django:
    ```bash
    python manage.py createsuperuser
    ```

6. Khởi động máy chủ phát triển:
    ```bash
    python manage.py runserver
    ```

7. Mở trình duyệt web của bạn và truy cập vào 'http://localhost:8000' để truy cập trang web.
