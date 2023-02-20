import Main

print("Test Main")


def test_BatteryLessThan205():
    test_result = 0
    result = Main.CheckBatteryLevel(200)
    assert (result == test_result)


def test_BatteryLessThan510():
    test_result = 1
    result = Main.CheckBatteryLevel(500)
    assert (result == test_result)


def test_BatteryLessThan512():
    test_result = 2
    result = Main.CheckBatteryLevel(511)
    assert (result == test_result)


def test_BatteryLessThan820():
    test_result = 3
    result = Main.CheckBatteryLevel(800)
    assert (result == test_result)


def test_BatteryMoreThan820():
    test_result = 4
    result = Main.CheckBatteryLevel(1000)
    assert (result == test_result)


def test_FuelLessThan20():
    test_result = 0
    result = Main.CheckFuelLevel(15)
    assert (result == test_result)


def test_FuelLessThan50():
    test_result = 1
    result = Main.CheckFuelLevel(40)
    assert (result == test_result)


def test_FuelLessThan100():
    test_result = 2
    result = Main.CheckFuelLevel(60)
    assert (result == test_result)


def test_FuelMoreThan100():
    test_result = 3
    result = Main.CheckFuelLevel(200)
    assert (result == test_result)


def test_LightMoreThan700():
    test_result = 0
    result = Main.Light(800)
    assert (result == test_result)


def test_LightLessThan700():
    test_result = 1
    result = Main.Light(500)
    assert (result == test_result)


def test_CheckTempHumidityNone():
    test_result = 0
    result = Main.CheckTempHumidity(None)
    assert (result == test_result)


def test_CheckTempHumidityValue():
    test_result = 1
    result = Main.CheckTempHumidity(10)
    assert (result == test_result)