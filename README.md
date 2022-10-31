Technical test exercises
=====================

1- Modified the current request bin service to accept and create bins with a given key. 
Also added the following required validations :

- Name is an alphanumeric 8 digits String.
- If name does not match previous statement request should fail with a 422 error that has body

2- Created the tests validating package_created_webhook 
 in folder back_tests you will find everything related to the test framework
 To be able to run the test you will need to have python3 and pip installed and execute the following commands:

```
$ pip install virtualenv
$ virtualenv backend_venv
$ source backend_venv/bin/activate
$ pip install -r back_tests/requirements.txt
$ BASE_URL="http://127.0.0.1:8888" python -m pytest -vs back_tests/tests/test.py
```

3- You can find the pipeline proposal on this files:
 Another option for this is deploy the service in Heroku and run the tests against that endpoint (it will reduce the pipeline time a lot as well)

```
.gitlab-ci.yml
.gitlab/ci/test.yml
template.yml
```

To trigger the test you can create a schedule in gitlab or do it manually by adding `TRIGGER_TEST = requestbin-api`
(We can see a demo during technical review)

4- One way that this can be achieved is to create all the configuration in the computers of these users (installation of Android Studio + Xcode) and in the case of android create an emulator. Then :

 - ANDROID
    just create a bash file like `android_emulator.command` with the content:
    ```
    #!/bin/bash
    emulator @Nexus_4_API_25
    ```

    being Nexus_4_API_25 the name of the emualtor created

 - iOS
    just create a bash file like `iOS_simulator.command` with the content:
    ```
    #!/bin/bash
    open -a Simulator.app
    ```

After that the user only needs to execute those bash files by clicking it to and emulator/simulator will start running for them.
(We can see a demo during technical review)