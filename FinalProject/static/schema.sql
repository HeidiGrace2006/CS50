CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    hash TEXT NOT NULL
);

CREATE TABLE user_stories (
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    choices_made INTEGER NOT NULL DEFAULT 0,
    current_segment REAL NOT NULL DEFAULT 1.1,
    PRIMARY KEY (user_id, title),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
