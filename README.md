## Overview

This Flask API models a Late Show system with **Episodes**, **Guests**, and **Appearances**. It allows you to retrieve episodes and guests, create appearances, and view nested relationships.

---

## Setup

1. **Clone the repository (private)**:

```bash
git clone <repo-url>
cd lateshow-firstname-lastname
```

2. **Create a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Run database migrations**:

```bash
flask db init
flask db migrate
flask db upgrade
```

5. **Seed the database** (optional):

```bash
python seed.py
```

6. **Run the app**:

```bash
python app.py
```

The API will run at `http://127.0.0.1:5000/`.

---

## Endpoints

### Episodes

* **GET /episodes**
  Returns all episodes:

```json
[
  {"id": 1, "date": "1/11/99", "number": 1},
  {"id": 2, "date": "1/12/99", "number": 2}
]
```

* **GET /episodes/<id>**
  Returns a single episode with appearances:

```json
{
  "id": 1,
  "date": "1/11/99",
  "number": 1,
  "appearances": [
    {
      "id": 1,
      "rating": 4,
      "episode_id": 1,
      "guest_id": 1,
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      }
    }
  ]
}
```

Returns `404` if episode does not exist:

```json
{"error": "Episode not found"}
```

### Guests

* **GET /guests**
  Returns all guests:

```json
[
  {"id": 1, "name": "Michael J. Fox", "occupation": "actor"},
  {"id": 2, "name": "Tracey Ullman", "occupation": "television actress"}
]
```

### Appearances

* **POST /appearances**
  Create a new appearance:

```json
{
  "rating": 5,
  "episode_id": 2,
  "guest_id": 2
}
```

Success response:

```json
{
  "id": 2,
  "rating": 5,
  "episode_id": 2,
  "guest_id": 2,
  "episode": {"id": 2, "date": "1/12/99", "number": 2},
  "guest": {"id": 2, "name": "Tracey Ullman", "occupation": "television actress"}
}
```

Validation error response:

```json
{"errors": ["validation errors"]}
```

---

## Notes

* `Appearance.rating` must be **between 1 and 5**.
* Deleting a Guest or Episode **cascades** to delete related Appearances.
* Serialization rules prevent recursion in nested JSON responses.
