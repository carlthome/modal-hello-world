# Modal Hello World

Toy example to test Modal.

## Install

```sh
# Install client in a Python virtual environment.
direnv allow
pip install -r requirements.txt

# Register client with a new token.
modal token new
```

## Run

```sh
modal run main.py
```

You should see something like

```sh
✓ Initialized. View app at https://modal.com/apps/[...]
✓ Created objects.
├── 🔨 Created square.
└── 🔨 Created mount [...]/modal-hello-world/main.py
This code is running on a remote worker!
the square is 1764
✓ App completed.
```
