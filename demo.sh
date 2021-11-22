rem chrome
pytest -s -v -m "sanity" --html=Reports/sanitysample_chrome.html /home/ticvictech/PycharmProjects/nopcommerceProject/testCases/ --browser chrome
REM pytest -s -v -m "sanity or regression" --html=Reports/sanitysample.html /home/ticvictech/PycharmProjects/nopcommerceProject/testCases/ --browser chrome
REM pytest -s -v -m "sanity and regression" --html=Reports/sanitysample.html /home/ticvictech/PycharmProjects/nopcommerceProject/testCases/ --browser chrome
REM pytest -s -v -m "regression" --html=Reports/sanitysample.html /home/ticvictech/PycharmProjects/nopcommerceProject/testCases/ --browser chrome

rem firefox
rem pytest -s -v -m "sanity" --html=Reports/sanitysample_firefox.html /home/ticvictech/PycharmProjects/nopcommerceProject/testCases/ --browser firefox
REM pytest -s -v -m "sanity or regression" --html=Reports/sanitysample.html /home/ticvictech/PycharmProjects/nopcommerceProject/testCases/ --browser firefox
REM pytest -s -v -m "sanity and regression" --html=Reports/sanitysample.html /home/ticvictech/PycharmProjects/nopcommerceProject/testCases/ --browser firefox
REM pytest -s -v -m "regression" --html=Reports/sanitysample.html /home/ticvictech/PycharmProjects/nopcommerceProject/testCases/ --browser firefox


