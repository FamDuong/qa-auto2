This project use pytest, pytest-bdd and pytest-html to create beautiful report with screenshot
To run the test, please run the below example command line

pytest Test_Runner.py --html=report.html

// Run pytest and publish result to testrail
py.test --testrail --tr-config=testrail.cfg --tr-plan-id=712 Test_Runner.py --tr-skip-missing --html=report.html

py.test --testrail --tr-config=testrail.cfg testscripts\smoketest\settings\general.py --tr-plan-id=712 --tr-skip-missing --html=report.html

// Test auto build in jenkins
// Test auto build in jenkins