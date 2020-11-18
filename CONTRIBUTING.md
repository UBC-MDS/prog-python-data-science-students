
## Contributing

### Contributions to the Dockerfile:

Ready to contribute to the Dockerfile? Here's how:

1. Clone the repository locally:

	```
	git clone git@github.com:UBC-MDS/prog-python-data-science-students.git
	```

2. Create a branch for local development:

	```
	git checkout -b name-of-your-bugfix-or-feature
	```

   	Now you can make your changes locally.

3. When you're done making changes, check that you can build the image locally via:

	```
	docker build --tag testimage dockerfiles/dsci-011/.
	```

4. Also test that you can run, grade and generate feedback for the course assignments using assignments from the instructors repo.

5. Commit your changes and push your branch to GitHub:

	```
	git add .
	git commit -m "Your detailed description of your changes."
	git push origin name-of-your-bugfix-or-feature
	```

6. Submit a pull request through the GitHub website and assign ttimbers to review it.
