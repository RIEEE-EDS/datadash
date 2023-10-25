# RIEEE DataDash

RIEEE DataDash is a lightweight, open-source, two-factor secure web application platform purpose-built to facilitate the innovative research of Research Institute of Environment, Energy, and Economics partners here at AppState.

With DataDash, RIEEE has developed full-stack capacity for secure, highly interactive web applications for research - no expensive or restrictive third-party software licenses required, and no strategic classroom-freemium model.

RIEEE also hopes to expand data science competency on campus and significantly lower the threshold for research application development and maintenence. To achieve this, we have been developing this platform with self-documentation practices, open access guides, templates, and educational resources for application development.

## Development Notes

### July 13th, 2023

- Come back to the idea of unlisted embedded applications if and only if that really seems necessary.  They can always be added as-needed later.

- **Can we get the gmail pfp from logged in users?**  My research on Shibboleth integration suggests we can, so until that's set up, there is a placeholder icon in the eastern header.

- **Digital accessibility policy?** Ask Jeff if he knows anything about complying with https://policy.appstate.edu/Digital_Accessibility

## Instructions

1. Clone the repository:

```shell
git https://github.com/mwhefner/datadash.git
```

2. Navigate to the project directory:

```shell
cd DataDash-application
```

3. Install the required dependencies (optionally, into a virtual environment):

```shell
pip install -r requirements.txt
```

4. Run datadash.py to run the application on http://127.0.0.1:8050/

```shell
python datadash.py
```


