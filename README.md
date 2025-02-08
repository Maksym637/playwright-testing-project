# playwright-testing-project
- - -
### Description:
A Playwright-based automated UI testing framework for the Amazon website
- - -
### Project structure:
Project has the following structure:
- `amazon` - Page Object Model (POM) for the website
- `tests` - Contains all test cases
- `utils` - Helper functions and utilities
- - -
### Technologies:
| Technology  | Version |
| ----------- | --------|
| Playwright  | 1.49.1  |
| Pytest      | 8.3.4   |
These libraries are built in the Python programming language
- - -
### Execute tests:
1. Install [Docker](https://docs.docker.com/get-started/get-docker/) on your local machine
2. Clone repository
3. Go to the `playwright-testing-project` directory
4. Build the Docker image:
```bash
docker-compose build
```
5. Start the service:
```bash
docker-compose up
```
PS: To remove all images, containers, and information in the cache, run the command:
```bash
docker system prune -a
```
- - -
