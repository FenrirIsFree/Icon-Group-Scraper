## Devcontainer

The devcontainer is a Docker container that is used to run the application. It is used to ensure that the application is run in a consistent environment.

The devcontainer is defined in the directoy `.devcontainer` with the `devcontainer.json` file being the main instructions for devcontainer setup which references the `Dockerfile` for the container instructions.

The devcontainer is then built using the `Dockerfile` in the root of the repository.

## Running the devcontainer

To run the devcontainer within an IDE that supports the devcontainer extension, you must do the following:

### Install devcontainer extension
Extension can be installed (here)["https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers"]

Once installed you can go to the extension which would be labeled as `Remote Explorer`. Click the `+` symbol and then select action `Open Current Folder in Container`. The window will re-open with the devcontainer environment following the dockerfile instructions.
