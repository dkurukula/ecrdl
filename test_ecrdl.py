import ecrdl

def test_dates():
    assert ecrdl.dates10m('2020-02-01', '2020-02-02')[0].year== 2020
    assert ecrdl.dates10m('2020-02-01', '2020-02-02')[0].month == 2
    assert ecrdl.dates10m('2020-02-01', '2020-02-02')[0].day == 1
    assert ecrdl.dates10m('2020-02-01', '2020-02-02')[0].hour == 0
    assert ecrdl.dates10m('2020-02-01', '2020-02-02')[0].minute == 0
