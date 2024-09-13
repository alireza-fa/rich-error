# Rich Error

<a href="https://github.com/alireza-fa/rich-error?tab=readme-ov-file#english">English</a>

<a href="https://github.com/alireza-fa/rich-error?tab=readme-ov-file#persian">Persian</a>


<h3>English</h3>

Rich Error is an error management pattern in programming that allows you to store detailed information about errors and the various layers in which these errors occurred before reaching you. Based on the collected information, you can easily display appropriate error messages to users or other systems.

Unlike standard errors, which typically include just a message or error code, Rich Error can include additional information such as metadata, the operation that caused the error, lower-level errors, and any other relevant details.

## Why Do We Call It Rich Error?

1. **More Information**:  
   Rich Error can include the error message, error code, the name of the operation that caused the error, and any other type of information. This information can include metadata that helps in better understanding the issue.

2. **Nested Structure**:  
   Rich Error allows you to manage nested errors. This means that if an error is caused by another error, you can trace back to the root cause, ensuring that no error is overlooked.

3. **Simplifies Your Work**:  
   As demonstrated in the examples, Rich Error simplifies your tasks and makes your code more organized and cohesive.

If you’re still uncertain about using Rich Error, here are some additional benefits:

1. **Better Problem Diagnosis**:  
   With rich information about errors, development teams can identify and resolve issues faster and more accurately.

2. **Enhanced User Experience**:  
   When errors are presented clearly with sufficient information, the user experience improves significantly.

3. **Faster Development**:  
   Using Rich Error can accelerate your development process, based on my own experience.

4. **Compatibility with Other Systems**:  
   The structured and sufficient information provided by Rich Error can be easily transferred to other systems. For example, you can utilize Rich Error information in your logging systems.
   
## How to Write a Rich Error?

One of the best ways to address such questions is to see how more experienced individuals have implemented this and what recommendations they provide.

The Microsoft documentation, particularly in the ErrorDetail section of the API guidelines, offers valuable insights. A Rich Error can include several key properties that help you store comprehensive information about errors. Below is a concise explanation of each property.
https://github.com/microsoft/api-guidelines/blob/vNext/azure/Guidelines.md

1. **operation**  
   This indicates the operation in which the error occurred. For example, it could be the name of the method or function that led to the error.
   - **Best Practice**: 
     - Use descriptive naming for the operation to make it easily identifiable.
     - This property can help you quickly identify issues in logs and reports.  
     For example, if the function `get_user_by_id` is in the `user` package and the `crud` file, and the error occurs within this package, the operation value could be:
     ```python
     RichError(operation="user.crud.get_user_by_id")
     ```

2. **code**  
   This property represents the error code, which is usually a number or a specific identifier. This code specifically references the type of error and can be used for categorizing errors.
   - **Best Practice**: 
     - Based on my experience, use a dictionary to manage error codes easily. 
     - Codes should be unique and meaningful for easy identification and management.

   **Why Should Error Codes Be Unique?**  
   This approach can help in error management. The idea is that each type of error should have a unique code that is easily identifiable and categorizable.

   **Benefits of Using Unique Error Codes**:
   1. **Quick Error Identification**:  
      Each error code points to a specific type of issue, helping us quickly understand what kind of error occurred.
   2. **Error Categorization**:  
      With unique codes, you can easily categorize errors based on type or resource.
   3. **Better Guidance for Users**:  
      Providing error codes to users or support teams allows them to easily refer to documentation or resources related to that error.
   4. **Reduced Overlap**:  
      Having specific codes for each type of error reduces the chance of overlap between errors.

   **Example of Error Codes**:
   To implement these codes, you can use a dictionary or Enum. I prefer using a dictionary:
   ```python
   USER_NOT_FOUND = 40401
   INVALID_INPUT = 40001
   INTERNAL_SERVER_ERROR = 50001
   ACCESS_DENIED = 40301

   ERROR_TRANSLATION = {
       USER_NOT_FOUND: "User does not exist",
       INVALID_INPUT: "Invalid input",
       INTERNAL_SERVER_ERROR: "Internal server error",
       ACCESS_DENIED: "Access denied"
   }
   ```
   Using a dictionary, we can easily provide text descriptions for each error or even utilize i18n (I prefer that clients display the appropriate text in their desired language based on the code).

3. **message**  
   A message that describes what type of error occurred. This message typically provides users or developers with more information about the nature of the error.
   - **Best Practice**: 
     - Use clear and concise messages that are easy to understand.
     - Messages should differ based on the type of error and user access level (e.g., for end users, messages should be simpler without rich details).

4. **error**  
   This property may refer to the underlying error that led to the Rich Error. It could be an exception that provides more details about the issue.
   - **Best Practice**: 
     - Use this property to store nested errors, meaning if one error is caused by another, store it here.
     - Ensure that information related to the original error is stored completely and clearly.

5. **meta_data**  
   This property can include any additional information that may be useful for better understanding the issue. For example, it can contain information about the system state, user inputs, etc.
   - **Best Practice**: 
     - Use a dictionary to store metadata so that you can easily manage different types of data.
     - This information should be collected and analyzed based on the specific needs and context of the error.

## Now You're Familiar with Rich Error!

At this point, you have a solid understanding of Rich Error. Next, I will explain the `rich-error` package and how to use Rich Error effectively and efficiently.

The `rich-error` package supports all the features we discussed. Here are some key points to keep in mind when using the `rich-error` package:

1. **Align Your Codes with HTTP Codes**:  
   Try to make your error codes correspond to HTTP status codes. This way, your codes can easily be converted into HTTP error responses. For example, use codes like:
   ```python
   OK = 200_00
   USER_NOT_FOUND = 404_01
   USER_CONFLICT = 409_01
   ```
   The first three digits of the codes should match the HTTP codes, while the subsequent digits can be whatever you prefer. Typically, codes range from five to six digits. Depending on the size of your project, you might have more than 99 instances of a specific code like 404, but I believe two additional digits are usually sufficient.

2. **Include Useful Information**:  
   Make sure to include as much useful information as possible within the Rich Error to simplify debugging.

3. **Access Error Information Easily**:  
   You can easily access the information inside the error using the `get_error_info` function.

By following these guidelines, you can effectively implement and utilize Rich Error in your applications.


## Example Without Using Rich Error

Let's consider an example where our application handles requests using a structure where a handler processes requests via a service, and if necessary, the service interacts with a database using a repository.

### Types of Errors That May Occur

Several types of errors may occur during this process. An error could happen in the repository and be returned to the service, which may also encounter its own set of errors. Ultimately, the handler should provide an appropriate response to the user.

Using Rich Error allows us to maintain a good log of errors as well as present a suitable response to the user. Here's how the code structure looks:

### `codes.py`
```python
OK = 200_00
USER_NOT_FOUND = 404_01
USER_CONFLICT = 409_01
IP_BLOCKED = 403_01
TOO_MANY_REQUEST = 429_01
INTERNAL_SERVER_ERROR = 500_01

ERROR_TRANSLATION = {
    OK: "ok",
    USER_NOT_FOUND: "user does not exist",  # We can use i18n for error translations, but I prefer not to.
    INTERNAL_SERVER_ERROR: "unexpected error",
    USER_CONFLICT: "this user already exists",
    IP_BLOCKED: "IP blocked",
    TOO_MANY_REQUEST: "too many requests",
}
```

### `api.py`
```python
from typing import Dict
from rich_error.utils.http.response import BaseResponse
from rich_error.utils.http.response import base_response as base_res
from rich_error.utils.http.response import base_response_with_error as base_res_error
from examples.with_rich_error.codes import OK, ERROR_TRANSLATION

def base_response(result: Dict | None, status_code: int = 200) -> BaseResponse:
    return base_res(status_code=status_code, code=OK, result=result)

def base_response_with_error(error: Exception):
    return base_res_error(error=error, error_translation=ERROR_TRANSLATION, code_k=100)
```

### `repository.py`
```python
from examples.with_rich_error.codes import USER_NOT_FOUND
from rich_error.error import RichError

class UserRepository:
    Op = "example.web.repository.UserRepository."

    def get_user_by_id(self, user_id: int):
        op = self.Op + "get_user_by_id"
        raise RichError(op).set_msg("User with this ID %d not found" % user_id).set_code(USER_NOT_FOUND)

def get_user_repository():
    return UserRepository()
```

### `service.py`
```python
import random
from abc import ABC, abstractmethod
from logging import error
from examples.with_rich_error import codes
from examples.with_rich_error.repository import get_user_repository
from rich_error.error import RichError, get_error_info

class Repository(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id):
        pass

class UserService:
    Op = "examples.web.service.UserService."

    def __init__(self, repo: Repository):
        self.repo = repo

    def get_user_by_id(self, user_id: int):
        op = self.Op + "get_user_by_id"
        meta = {"user_id": user_id}

        try:
            match random.randint(1, 5):
                case 1:
                    raise RichError(op).set_code(codes.USER_CONFLICT)
                case 2:
                    raise RichError(op).set_code(codes.TOO_MANY_REQUEST)
                case 3:
                    raise RichError(op).set_code(codes.IP_BLOCKED)
                case (4, 5):
                    return self.repo.get_user_by_id(user_id=user_id)

            return self.repo.get_user_by_id(user_id=user_id)
        except Exception as err:
            """
            Since we have used Rich Error throughout the system, we know that the lower layer has handled it,
            and we just need to propagate the error.
            """
            # log error self.logger.error(...)
            rich_err = RichError(op).set_error(err).set_meta(meta)
            error(msg=get_error_info(error=rich_err))
            raise rich_err

def get_user_service():
    return UserService(repo=get_user_repository())
```

### `handler.py`
```python
from examples.with_rich_error.service import get_user_service
from examples.with_rich_error.api import base_response_with_error, base_response

service = get_user_service()


def get_user_handler(user_id: int):
    try:
        return base_response(result=service.get_user_by_id(user_id=user_id))
    except Exception as err:
        return base_response_with_error(error=err)


if __name__ == "__main__":
    print(get_user_handler(user_id=1))
```

### error info:
```shell
ERROR:root:[{'Operation': 'examples.web.service.UserService.get_user_by_id', 'Code': 40401, 'Message': 'user with this id 1 not found', 'Meta': {'user_id': 1}}, {'Operation': 'example.web.repository.UserRepository.get_user_by_id', 'Code': 40401, 'Message': 'user with this id 1 not found', 'Meta': {}}]
```

By using Rich Error, we can log errors effectively and provide meaningful responses to users, enhancing both debugging and user experience.


## The Drawback of Not Using Rich Error

If we didn't use Rich Error, we would have to handle different errors using alternative solutions, such as defining specific exceptions for each error type. For example, we might write:

```python
class UserNotFoundErr(Exception):
    pass

class IpBlockedErr(Exception):
    pass

class TooManyRequestErr(Exception):
    pass

class UserConflictErr(Exception):
    pass
```

In the handler, we would also need to define these exceptions:

```python
from examples.without_rich_error.service import get_user_service
from examples.without_rich_error.exception import UserNotFoundErr, UserConflictErr, TooManyRequestErr, IpBlockedErr

service = get_user_service()

def get_user_handler(user_id: int):
    try:
        print(service.get_user_by_id(user_id=user_id))
    except UserNotFoundErr as err:
        print("User not found, code is 404:", err)
    except UserConflictErr as err:
        print("User conflict, code is 409:", err)
    except TooManyRequestErr as err:
        print("Too many requests, code is 429:", err)
    except IpBlockedErr as err:
        print("IP blocked, code is 403:", err)

if __name__ == "__main__":
    print(get_user_handler(user_id=1))
```

### Challenges with This Approach

1. **Increased Duplication**: As the number of exceptions grows, managing them becomes increasingly complex and leads to code duplication.
  
2. **Reduced Observability**: The system's ability to provide insights into errors diminishes. In contrast, using Rich Error allows us to capture all errors occurring at various layers, maintaining a comprehensive view of the error landscape.

By leveraging Rich Error, we can simplify error management, reduce duplication, and enhance the observability of our error handling mechanism.


<div dir="rtl">

<h3>Persian</h3>

ارور ثروتمند و یا RichError (https://github.com/alireza-fa/rich-error)

ریج ارور یک الگوی مدیریت خطا در برنامه‌نویسی است که به شما این امکان رو می‌ده تا اطلاعات دقیق‌تری درباره خطاها ها و لایه های مختلفی که این خطا رخ داده تا در نهایت به دست شما رسیده ذخیره کنید و بر اساس این اطلاعات جمع آوری شده، به کاربر یا سیستم‌های دیگه ارور و پیغام مناسب رو به راحتی نمایش بدید.

 بر خلاف خطاهای استاندارد که معمولاً فقط شامل یک پیام یا کد خطا هستند، RichError میتونه شامل اطلاعات اضافی مثل متا دیتا، اپریشنی که توش خطا رخ داده، ارور های لایه پایین تر و هر اطلاعاتی که بدردتون میخوره رو داشته باشید.

چرا بهش Rich error میگیم؟

1. اطلاعات بیشتر: 
   - ریچ ارور میتونه شامل پیام خطا، کد خطا، نام عملی که باعث خطا شده و هر نوع اطلاعات دیگه باشه. این اطلاعات میتونن شامل متا دیتاهایی باشن که به درک بهتر مشکل کمک میکنن(خیلی کمک میکنن).

2. ساختار تو در تو: 
   - ریچ ارور می‌تونه به شما اجازه بده که خطاهای تو در تو رو مدیریت کنید. به این معنی که اگر یک خطا ناشی از یک خطای دیگه باشه میتونید به خطای اصلی برسید و درواقع خطایی از دست نمیره.

3. خیلی کارتونو راحت تر میکنه: 
   - تو مثال هایی که براتون زدم میفهمید که چقدر کارتون رو ساده تر میکنه همچنین باعث میشه کدتون منظم تر و یکپارچه بشه.

اگه هنوز درباره استفاده از Rich error دودلی اینم چند مورد دیگه از مزایاش:

1. تشخیص بهتر مشکلات: 
   - با داشتن اطلاعات غنی درباره خطاها، تیم‌های توسعه میتونن سریع‌تر و دقیق‌تر مشکلات رو شناسایی و حل کنن.

2. تجربه کاربری بهبود یافته: 
   - وقتی که خطاها به صورت واضح و با اطلاعات کافی به کاربر نمایش داده بشه، تجربه کاربری خیلی بهتر میشه.

3. توسعه سریع‌تر: 
   - با استفاده از RichError، سرعت توسعتون بیشتر میشه(طبق تجربه خودم)

5. سازگاری با سیستم‌های دیگه: 
   - اطلاعات کافی و ساختارمند ریچ ارور میتونه به راحتی به سیستم‌های دیگر منتقل بشه مثلا میتونید توی لاگرتون هم از اطلاعات ریچ ارور استفاده کنید.

چطور یک Rich error بنویسیم؟
یکی از بهترین کارها برای رسیدن به جواب سوال های این چنینی این هستش ببینیم افراد خفن تر و باتجربه تر چطور پیاده کردن و چه پیشنهاد هایی رو به ما میدن.

توی داکیومنت microsoft قسمت ErrorDetail در api guideline یه سری توضیحات خوبی داده.
https://github.com/microsoft/api-guidelines/blob/vNext/azure/Guidelines.md

یک ریچ ارور میتونه شامل چندین پراپرتی کلیدی باشه که به شما کمک میکنه اطلاعات جامع‌تری درباره خطاها ذخیره کنید. در ادامه به توضیح شسته رفته درباره هر پراپرتی میپردازیم.

1. operation
نشاندهنده عملی است که خطا در آنجا اتفاق افتاده است. به عنوان مثال، میتونه نام متد یا عملکردی باشه که منجر به بروز خطا شده.
- بهترین شیوه:
  - از نام‌گذاری توصیفی برای عملیات استفاده کنید تا به راحتی قابل شناسایی باشه.
  - این پراپرتی میتونه به شما کمک کنه تا در لاگ‌ها و گزارش‌ها، مشکل را سریع‌تر شناسایی کنید.
مثلا فرض کنید فانکش get_user_by_id در پکیج user و فایلی به نام crud قرار دارد و ارور داخل این پکیج رخ میدهد.
مقدار operation میتونه این باشه:
RichError(operation="user.crud.get_user_by_id")

2. code
- پراپرتی کد خطا را نمایش میده که معمولاً یک عدد یا شناسه خاص است. این کد به طور خاص به نوع خطا اشاره داره و میتونه برای دسته‌بندی خطاها استفاده بشه.
- بهترین شیوه:
  برای نگهداری کد های خطا طبق تجربه من از یک dictionaty میتونید استفاده کنید تا مدیریت اونها آسون تر باشه.
  - کدها باید به صورت یکتا و معنادار باشن تا به راحتی قابل شناسایی و مدیریت باشند.

چرا کد های خطا یکتا باشند؟
این روش میتونه به مدیریت خطاها کمک کنه. ایده این است که هر نوع خطا یک کد منحصر به فرد داشته باشه که به راحتی قابل شناسایی و دسته‌بندی باشه.

مزایای استفاده از کدهای خطای منحصر به فرد

1. شناسایی سریع خطاها:
   - هر کد خطا به نوع خاصی از مشکل اشاره داره و به کمک میکنه تا به سرعت بفهمیم که چه نوع خطایی رخ داده است.

2. دسته‌بندی خطاها:
   - با داشتن کدهای منحصر به فرد، می‌توانید خطاها را به راحتی دسته‌بندی کنید و آن‌ها را بر اساس نوع یا ریسورس طبقه‌بندی کنید.

3. راهنمایی بهتر برای کاربران:
   - با ارائه کد خطا به کاربران یا تیم پشتیبانی، میتونن به راحتی به مستندات یا منابع مرتبط با اون خطا مراجعه کنن.

4. کاهش احتمال تداخل:
   - با داشتن کدهای خاص برای هر نوع خطا، احتمال تداخل بین خطاها کاهش پیدا میکنه.

مثال از کدهای خطا

برای پیاده‌سازی این کدها می‌توانید از یک دیکشنری یا Enum استفاده کنید. که من از دیکشنری استفاده می کنم:
</div>

```python
USER_NOT_FOUND = 40401
INVALID_INPUT = 40001
INTERNAL_SERVER_ERROR = 50001
ACCESS_DENIED = 40301

ERROR_TRANSLATION = {
    USER_NOT_FOUND: "user does not exists",
    INVALID_INPUT: "invalid input",
    INTERNAL_SERVER_ERROR: "internal server error",
    ACCESS_DENIED: "access denied"
}
```

<div dir="rtl">
 با استفاده از دیکشنری میتوانیم به راحتی معنی هر ارور را بصورت تکست بنویسیم و یا حتی از i18n استفاده کنیم(من ترجیح میدم بر اساس کد کلاینت ها خودشون متن مناسب رو به هر زبونی که میخوان نشون بدن)

3. message
پیامی است که توصیف می‌کند چه نوع خطایی رخ داده است. این پیام معمولاً به کاربر یا توسعه‌دهنده اطلاعات بیشتری درباره ماهیت خطا میدهد.
- بهترین شیوه:
  - از پیام‌های واضح و مختصر استفاده کنید که به راحتی قابل درک باشند.
  - پیام‌ها باید با توجه به نوع خطا و سطح دسترسی کاربر متفاوت باشن (مثلاً برای کاربران نهایی مثلا کلاینت ها پیام‌ها باید ساده‌تر باشن و اطلاعات rich ندیم).

4. error
این ویژگی میتونه به خطای اصلی که منجر به بروز RichError شده اشاره داشته باشه. این میتونه یک استثنا (Exception) باشه که اطلاعات بیشتری درباره مشکل ارائه میده.
- بهترین شیوه:
  - از این ویژگی برای نگهداری خطاهای تو در تو استفاده کنید، یعنی اگر یک خطا ناشی از خطای دیگری باشد، آن را در این پراپرتی ذخیره کنید.
  - اطمینان حاصل کنید که اطلاعات مربوط به خطای اصلی به طور کامل و واضح ذخیره شده باشه.

5. meta_data
 این پراپرتی میتونه شامل هر نوع اطلاعات اضافی باشه که ممکنه  برای درک بهتر مشکل مفید باشن. به عنوان مثال، اطلاعات مربوط به وضعیت سیستم، ورودی‌های کاربر و غیره.
- بهترین شیوه:
  - از یک دیکشنری برای نگهداری اطلاعات متا استفاده کنید تا به راحتی بتونید داده‌های مختلف رو ذخیره کنید.
  - این اطلاعات باید بر اساس نیاز و موقعیت خاص خطا جمع‌آوری و تحلیل بشن.


خب تا اینجای کار شما بخوبی با rich error آشنایی شدید.
در ادامه درباره پکیج rich-error توضیح میدم و نحوه استفاده درست و مفید از rich error رو بهتون میگم.

پکیج rich error تمامی مواردی که درباره اش توضیح دادیم رو پشتیبانی می کند.
نکاتی که برای استفاده از پکیج rich error وجود داره رو بهتون میگم:
اولین مورد این هستش سعی کنید کد هاتون متناسب با http code ها باشه در این صورت خیلی راحت کدهای شما به http error response تبدیل می شود.
مثلا از کد های زیر استفاده کنید:

</div>

```python
OK = 200_00
USER_NOT_FOUND = 404_01
USER_CONFLICT = 409_01
```

<div dir="rtl">

سه رقم اول کد ها، مساوی با http code باشد و رقم های بعدی هرچه دوست دارید.
معمولا کد ها پنج تا شش رقمی هستند. این به پروژه شما بستگی دارد اگر پروژه بزرگی است ممکن است بیش از 99 تا 404 داشته باشید اما بنظر من دو رقم کافی است.
سعی کنید تا جای ممکن اطلاعات مفید را داخل rich error قرار دهید تا دیباگ کردن راحت تر شود.
همچنین با تابع get_error_info به راحتی به اطلاعات داخل ارور دسترسی پیدا میکنید.


حالا بیاید یک مثال بدون استفاده از rich error بزنیم
برنامه ما به این صورت عمل میکند که handler ریکوئست هارا می گیرد سپس handler ریکوئست هارا با استفاده از service پراسس میکند و اگر نیاز بود service با دیتابیس کاری داشته باشد، از repository استفاده میکند.

چند نوع ارور ممکن است رخ بدهد
یکی از ارور ها در repository اتفاق میوفتد و به service برمیگردد خود سرویس هم ممکن است یک سری ارور هایی رخ بدهد.
در نهایت handler باید پاسخ مناسب رو به کاربر نشان بدهد.
ما با استفاده از rich error هم تونستیم یک لاگ خوب از ارور ها بزنیم همچنین یک پاسخ مناسب رو به کاربر نشون بدیم:

</div>

### `codes.py`
```python
OK = 200_00
USER_NOT_FOUND = 404_01
USER_CONFLICT = 409_01
IP_BLOCKED = 403_01
TOO_MANY_REQUEST = 429_01
INTERNAL_SERVER_ERROR = 500_01

ERROR_TRANSLATION = {
    OK: "ok",
    USER_NOT_FOUND: "user does not exist",  # We can use i18n for error translations, but I prefer not to.
    INTERNAL_SERVER_ERROR: "unexpected error",
    USER_CONFLICT: "this user already exists",
    IP_BLOCKED: "IP blocked",
    TOO_MANY_REQUEST: "too many requests",
}
```

### `api.py`
```python
from typing import Dict
from rich_error.utils.http.response import BaseResponse
from rich_error.utils.http.response import base_response as base_res
from rich_error.utils.http.response import base_response_with_error as base_res_error
from examples.with_rich_error.codes import OK, ERROR_TRANSLATION

def base_response(result: Dict | None, status_code: int = 200) -> BaseResponse:
    return base_res(status_code=status_code, code=OK, result=result)

def base_response_with_error(error: Exception):
    return base_res_error(error=error, error_translation=ERROR_TRANSLATION, code_k=100)
```


### `repository.py`
```python
from examples.with_rich_error.codes import USER_NOT_FOUND
from rich_error.error import RichError

class UserRepository:
    Op = "example.web.repository.UserRepository."

    def get_user_by_id(self, user_id: int):
        op = self.Op + "get_user_by_id"
        raise RichError(op).set_msg("User with this ID %d not found" % user_id).set_code(USER_NOT_FOUND)

def get_user_repository():
    return UserRepository()
```

### `service.py`
```python
import random
from abc import ABC, abstractmethod
from logging import error
from examples.with_rich_error import codes
from examples.with_rich_error.repository import get_user_repository
from rich_error.error import RichError, get_error_info

class Repository(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id):
        pass

class UserService:
    Op = "examples.web.service.UserService."

    def __init__(self, repo: Repository):
        self.repo = repo

    def get_user_by_id(self, user_id: int):
        op = self.Op + "get_user_by_id"
        meta = {"user_id": user_id}

        try:
            match random.randint(1, 5):
                case 1:
                    raise RichError(op).set_code(codes.USER_CONFLICT)
                case 2:
                    raise RichError(op).set_code(codes.TOO_MANY_REQUEST)
                case 3:
                    raise RichError(op).set_code(codes.IP_BLOCKED)
                case (4, 5):
                    return self.repo.get_user_by_id(user_id=user_id)

            return self.repo.get_user_by_id(user_id=user_id)
        except Exception as err:
            """
            Since we have used Rich Error throughout the system, we know that the lower layer has handled it,
            and we just need to propagate the error.
            """
            # log error self.logger.error(...)
            rich_err = RichError(op).set_error(err).set_meta(meta)
            error(msg=get_error_info(error=rich_err))
            raise rich_err

def get_user_service():
    return UserService(repo=get_user_repository())
```

### `handler.py`
```python
from examples.with_rich_error.service import get_user_service
from examples.with_rich_error.api import base_response_with_error, base_response

service = get_user_service()


def get_user_handler(user_id: int):
    try:
        return base_response(result=service.get_user_by_id(user_id=user_id))
    except Exception as err:
        return base_response_with_error(error=err)


if __name__ == "__main__":
    print(get_user_handler(user_id=1))
```

### error info:
```shell
ERROR:root:[{'Operation': 'examples.web.service.UserService.get_user_by_id', 'Code': 40401, 'Message': 'user with this id 1 not found', 'Meta': {'user_id': 1}}, {'Operation': 'example.web.repository.UserRepository.get_user_by_id', 'Code': 40401, 'Message': 'user with this id 1 not found', 'Meta': {}}]
```

<div dir="rtl">
با استفاده از rich error تجربه کاربری افزایش پیدا میکند همچنین دیباگینگ و لاگینگ نیز بهتر می شود.

اما اگر از rich error استفاده نمیکردیم، برای هندل کردن ارور های مختلف مجبور بودیم از یک سولوشن دیگر بجز exception استفاده کنیم و یا اینکه بیایم و برای هر ارور به این صورت exceptionبنویسیم:

</div>

```python
class UserNotFoundErr(Exception):
    pass

class IpBlockedErr(Exception):
    pass

class TooManyRequestErr(Exception):
    pass

class UserConflictErr(Exception):
    pass
```

<div dir="rtl">
در handler هم باید این کار رو میکردیم:

</div>

```python
from examples.without_rich_error.service import get_user_service
from examples.without_rich_error.exception import UserNotFoundErr, UserConflictErr, TooManyRequestErr, IpBlockedErr

service = get_user_service()

def get_user_handler(user_id: int):
    try:
        print(service.get_user_by_id(user_id=user_id))
    except UserNotFoundErr as err:
        print("User not found, code is 404:", err)
    except UserConflictErr as err:
        print("User conflict, code is 409:", err)
    except TooManyRequestErr as err:
        print("Too many requests, code is 429:", err)
    except IpBlockedErr as err:
        print("IP blocked, code is 403:", err)

if __name__ == "__main__":
    print(get_user_handler(user_id=1))
```

<div dir="rtl">

در این صورت هرچقدر تعداد exceptionها بیشتر شود duplicate و مدیریت کردن آنها نیز سخت تر خواهد شد. همچنین قدرت مشاهده گری سیستم با استفاده از exception ها نیز پایین می آید در صورتی که ما در rich error تمامی ارور هایی که در لایه های مختلف رخ داده باشن رو داشتیم.

اگر این ریپوزیتوری برای شما مفید بود، ممنون میشم با معرفی و ستاره دادن حمایت کنید
</div>
