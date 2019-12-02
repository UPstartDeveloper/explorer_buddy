# Explorer Buddy
They say we have more information available us today than ever before - but does that make us more knowledgeable?
Learning is about asking questions, not just looking up answers others have found for you.
Explorer Buddy is a note taking app for the most curious among us - children, who want a companion
to help take ownership over the questions they want answered about the world around us.
Explorer Buddy will allow users to discover knowledge through jotting down their own observations,
asking their own burning questions, and testing their own hypotheses - all while beating traditional paper notebooks with its modern web UI/UX.
Will you help develop Explorer Buddy to be the *cutting-edge* learning resource of the future?

## Proposal
Please look at [proposal.md](proposal.md) for why young scientists everywhere will
benefit from Explorer Buddy.

## Getting Started
### Prerequisites
- Must have Git installed
- Must have a GitHub account
- Must have Python 3.7.4 or later
- Must know how to work in a [Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/)
(Docker should work as well, I've just never used it before)

### How to Contribute To This Project:
These instructions will help you get a copy of the repository up and running on your local machine.
- Fork this repository (click the "Fork" button at the top right of the page, then click on your profile image).
- Clone your forked repository onto your local machine
```
git clone hhttps://github.com/<YOUR_GITHUB_USERNAME>/explorer_buddy.git
```
- Start your virtual environment, and be sure to see the 'Installing Requirements' section below to make sure you have all the required dependencies!

- Create a new branch for the feature you want to work on, or the bug fix you want to make:
```
git checkout -b feature/branch-name or bugfix/branch-name
```
- Make your changes (be sure to commit and push!)
```
git add .
git commit -m "[YOUR COMMIT MESSAGE HERE]"
git push origin branch-name
```
- Don't forget to add yourself to the [CONTRIBUTORS.md](CONTRIBUTORS.md) file!
Please credit your own work, by adding your name to the list in this format:
```
Name: [YOUR_NAME](Link to your GitHub Account, social media, or other personal link)
About Me: 2-3 sentences to introduce yourself
Feature: What did you contribute?
Technologies: What did you use to build your contribution?
Fun Fact: optional trivia about yourself!
```
- Create new Pull Request from your forked repository - Click the "New Pull Request" button located at the top of your repo
- Wait for your PR review and merge approval!
- If you care about this work, then I humbly ask you to **please star this repository and spread the word with more developers! Thank you!**

#### Installing Requirements
To ensure you have a development experience that's **as smooth as possible**, please follow these instructions:

- Once you have activated your Python virtual environment, please be sure to run the following command from the command line, to ensure you have all the dependencies
you may need to use for this project:
```
python3 -m pip install -r requirements.txt
```
- You may always double check the dependencies you have using this command:
```
python3 -m pip list
```
- If you install any new dependencies, please be sure to record them using
```
python3 -m pip freeze > requirements.txt
```
Thank you in advance for contributing to this project!

## Running the Tests
Within the `explorer_buddy/explorer` directory, you can run the tests for this project from the command line, using:
```
python3 manage.py test
```
If you would like to add tests of your own and don't know how, please be sure to read the [Django 2.2 documentation on testing](https://docs.djangoproject.com/en/2.2/topics/testing/overview/#).
If you are writing tests for the `api` package, you may also like to consult the [Django REST Framework documentation](https://www.django-rest-framework.org/api-guide/testing/).

## Built With
- Django - web framework for the backend
- Bootstrap 4 - styling the front end
- SQLite 3 - schema for the database (development)
- PostgreSql - production database schema
- Django REST Framework - framework building the API (found in the [explorer_buddy.explorer.api package](/explorer_buddy/explorer/api/)).

## Authors
- **Zain Raza** - *Initial work* - Make School Student, Data Science Concentration

## License
This project is licensed under the MIT License - see [LICENSE.md](LICENSE.md) for more details.

## Acknowledgements
- Mom and Dad - Thank you both for helping me discover a love of science from an early age.
None of what I accomplish at Make School would be possible without your support.
- [Django Project](https://www.djangoproject.com/) - This project's backend is built off the Django web framework for Python.
Thanks so much for all the open source contributions you guys are making!
- Dani Roxberry and Meredith Murphy (Make School BEW Instructors) - thank you both for helping me learn how to use the Django Web Framework!
- Billie Thompson - inspired this README.md file with her amazing [README.md template on GitHub Gist!](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
