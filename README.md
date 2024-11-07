# FlaskDiary
This project is a simple web-based diary application built with Flask. Users can create, edit, and delete diary entries, which are stored in a session for persistence during a single browser session.

**Keep your diary safe and secure!** All entries are stored temporarily on your local session, ensuring your thoughts remain private while you're using the app.

# Features
- **Create Diary Entries**: Users can write and save diary entries.
- **View Diary Entries**: Entries are displayed in reverse chronological order on the main page.
- **Edit Diary Entries**: Users can edit existing entries.
- **Delete Diary Entries**: Users can delete specific entries.
- **Session-Based Privacy**: All entries are stored in your session, keeping them private and secure during your browsing session.

# Usage
## Home Page:
- The home page displays all diary entries.
- Use the input form to add new entries.

## Edit an Entry:
- Click the "Edit" button next to an entry to modify it.

## Delete an Entry:
- Click the "Delete" button next to an entry to remove it.

# Security
- **Your diary stays private**. The app uses session storage, ensuring no data is saved once your session ends.
- The app.secret_key is used to sign session data. Replace 'your_secret_key' with a secure, random value in production.

https://github.com/user-attachments/assets/f92a4437-bd1b-483d-a9f6-40306901ce14
