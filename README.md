# MailBox
Email client app, using JavaScript. Users can send, receive, reply and archive emails through the app, which makes API calls to a Django back-end in order to send and receive 'emails', which are stored in an SQL database.

### Project Summary
The aim of the project is to build a front-end for a single-page email client app, using HTML and JavaScript. The page makes API calls to a Django back-end in order to send and receive emails between registered users. Emails between users are stored and read from a database on the back-end.

<img src="mail-inbox.png" alt="Screenshot of the project">
<hr>
<img src="mailbox.png" alt="Screenshot of the project">

[View the full assignment description on CS50's OpenCourseWare](https://cs50.harvard.edu/web/2020/projects/3/mail/)

### Technologies:

* Back-end:
  * Python
  * Django

* Front-end:
  * HTML
  * JavaScript
  * CSS (with some Bootstap Components)

### API Details:

The single-page front-end app uses calls to the applications API in order to:

* **Email Inbox**: Get all emails from a user's inbox (inbox, sent and archive inboxes available):
  * Send a `GET` request to `/emails/<mailbox>` where `<mailbox>` is either `inbox`, `sent`, or `archive` to receive in JSON form a list of all emails in the mailbox, in reverse chronological order. An email object looks like this:
  ```
  {
        "id": 100,
        "sender": "foo@example.com",
        "recipients": ["bar@example.com"],
        "subject": "Hello!",
        "body": "Hello, world!",
        "timestamp": "Jan 2 2020, 12:00 AM",
        "read": false,
        "archived": false
  }
    ```
  * Requesting a mailbox other than `inbox`, `sent` or `archive` will result in a JSON response of `{"error": "Invalid mailbox."}`

* **Single Email**: Get a single email by its unique ID:
  * Send a `GET` request to `/emails/<email_id>` where `email_id` is an integer id for an email, to receive a JSON representation of the single email (format as above).
  * If the requested email does not exist, or the user does not have access to this email, the route instead return a 404 Not Found error with a JSON response of `{"error": "Email not found."}`.

* **Sending Emails**: To send an email to the server:
  * Send a `POST` request to the `/emails` route. The route requires the body of the request to contain a JSON object containing the following:
    * a `recipients` value (a comma-separated string of all users to send an email to)
    * a `subject` string for the email subject
    * a `body` string for the main email text
  * For example:
```
{
      recipients: 'baz@example.com',
      subject: 'Meeting time',
      body: 'How about we meet tomorrow at 3pm?'
}
```
  * If the email is sent successfully, the route will respond with a 201 status code and a JSON response of `{"message": "Email sent successfully."}`
  * If no recipient is provided, the route will respond with a 400 status code and a JSON response of `{"error": "At least one recipient required."}`
  * If the receipient does not exist, instead the response will be `{"error": "User with email baz@example.com does not exist."}`

* **Mark Emails**: To archive/unarchive emails or mark individual emails as read/unread:
  * Sent a `PUT` request to `/emails/<email_id>` where `email_id` is the id of the email you're trying to modify. The route requires the body of the request to contain a JSON object with a key of either `archived` or `read` and a value of `true` or `false`.
    * `{archived: true}` will archive the email, `{archived: false}` will unarchive the message.
    * `{read: true}` will mark the email as read, `{read: false}` will mark the email as unread.

### Usage:

Requires Python(3) and the Python Pacakage Installer (pip) to run:
* Install requirements (Django): `pip install -r requirements.txt`
* Make and apply migrations to database:

```
python manage.py makemigrations mail
python manage.py migrate
```
* Run the app locally: `python manage.py runserver`
* Two separate accounts/logins will need to be created in order to send emails back and forth. A private browser window can be logged into a separate account.