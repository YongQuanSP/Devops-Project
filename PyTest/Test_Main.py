import Main

print("Test Main")


def test_Check_Battery():
    test_result = 0
    result = Main.CheckBatteryLevel(200)
    assert(result == test_result)


def test_Check_Fuel():
    test_result = 0
    result = Main.CheckFuelLevel(15)
    assert(result == test_result)


def test_Light():
    test_result = 0
    result = Main.Light(800)
    assert(result == test_result)


def test_CheckTempHumidity():
    test_result = 0
    result = Main.CheckTempHumidity(None)
    assert(result == test_result)
