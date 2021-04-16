from durable.lang import *

#저장용기는 종류별로 TYPE1,TYPE2,TYPE3,TYPE4 구분함.
#저장용기는 종류별로 최소압력, 최대압력 정상 범위 다름.
#저장용기는 수치가 최소압력이하일 경우 경고, 최대압력이상일 경우 위험
#압축기는 인입압력, 출구압력, 출구온도에 따라 위험 감지 다름.
#압축기는 인입압력 정상범위는 4MPa ~ 20MPa 임.
#압축기는 출구압력 정상범위는 40MPa ~ 90MPa 임.
#압축기는 출구온도 정상범위는 5℃ ~ 30℃ 임.
#압력가스시설 위험 경고 요소는 토출압력, 토출온도 임.
#압력가스시설 토출압력이 9kg/㎠ 이상인 경우 위험
#압력가스시설 토출온도가 140℃ 이상인 경우 위험
#가스감지기 신호 발생할 경우 위험
#불꽃검지기 신호 발생할 경우 위험
#긴급차단장치 신호 발생할 경우 위험
#운영신호기,미운영신호기는 운영신호와 미운영신호가 없는 경우, 미운영신호가 발생할 경우 경고
#냉각기는 냉각기 온도가 -60℃ 초과할 경우 경고

_PRINT = False
_warn_cnt = 0
_risk_cnt = 0
def warn(fact):
    global _warn_cnt
    _warn_cnt = _warn_cnt + 1

def risk(fact):
    global _risk_cnt
    _risk_cnt = _risk_cnt + 1

def warn_cnt():
    return _warn_cnt

def risk_cnt():
    return _risk_cnt

def init_cnt():
    _warn_cnt = 0
    _risk_cnt = 0

with ruleset('monitoring'):

    #룰1. 저장용기가 TYPE1이고, 최소압력이 3MPa 이하이면 경고, 최대압력이 48MPa 이상이면 위험
    @when_all(c.item << (m.name == 'storeTank') & (m.type == 'TYPE1') & (m.pressure > 0))
    def rule1(c):
        if c.item.pressure <= 3:
            warn({'t': c.item.type, 'p': c.item.pressure})
            if _PRINT:
                print('warn {0}'.format(_warn_cnt))
        elif c.item.pressure >= 48:
            risk({'t': c.item.type, 'p': c.item.pressure})
            if _PRINT:
                print('risk {0}'.format(_risk_cnt))

    #룰2. 저장용기가 TYPE2이고, 최소압력이 3MPa 이하이면 경고, 최대압력이 87MPa 이상이면 위험
    @when_all(c.item << (m.name == 'storeTank') & (m.type == 'TYPE2') & (m.pressure > 0))
    def rule2(c):
        if c.item.pressure <= 3:
            warn({'t': c.item.type, 'p': c.item.pressure})
            if _PRINT:
                print('warn {0}'.format(_warn_cnt))
        elif c.item.pressure >= 87:
            risk({'t': c.item.type, 'p': c.item.pressure})
            if _PRINT:
                print('risk {0}'.format(_risk_cnt))

    #룰3. 저장용기가 TYPE3이고, 최소압력이 3MPa 이하이면 경고, 최대압력이 100MPa 이상이면 위험
    @when_all(c.item << (m.name == 'storeTank') & (m.type == 'TYPE3') & (m.pressure > 0))
    def rule3(c):
        if c.item.pressure <= 3:
            warn({'t': c.item.type, 'p': c.item.pressure})
            if _PRINT:
                print('warn {0}'.format(_warn_cnt))
        elif c.item.pressure >= 100:
            risk({'t': c.item.type, 'p': c.item.pressure})
            if _PRINT:
                print('risk {0}'.format(_risk_cnt))

    #룰4. 저장용기가 TYPE4이고, 최소압력이 3MPa 이하이면 경고, 최대압력이 100MPa 이상이면 위험
    @when_all(c.item << (m.name == 'storeTank') & (m.type == 'TYPE4') & (m.pressure > 0))
    def rule4(c):
        if c.item.pressure <= 3:
            warn({'t': c.item.type, 'p': c.item.pressure})
            if _PRINT:
                print('warn {0}'.format(_warn_cnt))
        elif c.item.pressure >= 100:
            risk({'t': c.item.type, 'p': c.item.pressure})
            if _PRINT:
                print('risk {0}'.format(_risk_cnt))

    #룰5. 압축기 인입압력이 4MPa 이하이면 경고, 인입압력이 20MPa 이상이면 위험
    @when_all(c.item << (m.name == 'compressor'))
    def rule5(c):
        if c.item.inPressure < 4:
            warn({'t': c.item.type, 'p': c.item.pressure})
            if _PRINT:
                print('warn {0}'.format(_warn_cnt))
        elif c.item.inPressure > 20:
            risk({'t': c.item.type, 'p': c.item.pressure})
            if _PRINT:
                print('risk {0}'.format(_risk_cnt))

    #룰6. 압축기 출구압력이 40MPa 이하이면 경고, 출구압력이 90MPa 이상이면 위험
    @when_all(c.item << (m.name == 'compressor'))
    def rule6(c):
        if c.item.outPressure < 40:
            warn({'t': c.item.type, 'p': c.item.pressure})
            if _PRINT:
                print('warn {0}'.format(_warn_cnt))
        elif c.item.outPressure > 90:
            risk({'t': c.item.type, 'p': c.item.pressure})
            if _PRINT:
                print('risk {0}'.format(_risk_cnt))

    #룰7. 압축기 출구온도가 5℃ ~ 30℃ 이외일 경우 경고
    @when_all(c.item << (m.name == 'compressor'))
    def rule7(c):
        if ((c.item.temperature < 5) | (c.item.temperature > 30)):
            warn({'t': c.item.type, 'p': c.item.pressure})
            if _PRINT:
                print('warn {0}'.format(_warn_cnt))

    #룰8. 압력가스시설 토출압력이 9kg/㎠ 이상인 경우 위험
    @when_all(c.item << (m.name == 'compressorGas') & (m.pressure > 0))
    def rule8(c):
        if c.item.pressure >= 9:
            risk({'t': c.item.temperature, 'p': c.item.pressure})
            if _PRINT:
                print('risk {0}'.format(_risk_cnt))

    #룰9. 압력가스시설 토출온도가 140℃ 이상인 경우 위험
    @when_all(c.item << (m.name == 'compressorGas') & (m.pressure > 0))
    def rule9(c):
        if c.item.temperature >= 140:
            risk({'t': c.item.temperature, 'p': c.item.pressure})
            if _PRINT:
                print('risk {0}'.format(_risk_cnt))

    #룰10. 가스감지기의 가스가 감지될 경우 위험
    @when_all(c.item << (m.name == 'detectGas') & (m.detect == 'Y'))
    def rule10(c):
        risk({'n': c.item.index, 'd': c.item.detect})
        if _PRINT:
            print('risk {0}'.format(_risk_cnt))

    #룰11. 불꽃검지기의 불꽃이 검지될 경우 위험
    @when_all(c.item << (m.name == 'detectFlame') & (m.detect == 'Y'))
    def rule11(c):
        risk({'n': c.item.index, 'd': c.item.detect})
        if _PRINT:
            print('risk {0}'.format(_risk_cnt))

    #룰12. 긴급차단장치가 동작할 경우 위험
    @when_all(c.item << (m.name == 'breaker') & (m.detect == 'Y'))
    def rule12(c):
        risk({'n': c.item.index, 'd': c.item.detect})
        if _PRINT:
            print('risk {0}'.format(_risk_cnt))

    #룰13. 미운영신호가 발생할 경우 경고
    @when_all(c.item << (m.name == 'operator'))
    def rule13(c):
        if c.item.notOperate == '1':
            warn({'t': c.item.inOperate, 'p': c.item.notOperate})

        if _PRINT:
            print('warn {0}'.format(_warn_cnt))

    #룰14. 운영신호와 미운영신호가 없는 경우 경고
    @when_all(c.item << (m.name == 'operator'))
    def rule14(c):
        if (c.item.inOperate == '0' & c.item.notOperate == '0'):
            warn({'t': c.item.inOperate, 'p': c.item.notOperate})

        if _PRINT:
            print('warn {0}'.format(_warn_cnt))

    #룰15. 냉각기 온도가 -60℃ 초과할 경우 경고
    @when_all(c.item << (m.name == 'freezer'))
    def rule15(c):
        if float(c.item.temperature) > -60:
            warn({'t': c.item.inOperate, 'p': c.item.notOperate})

        if _PRINT:
            print('warn {0}'.format(_warn_cnt))

    @when_any(all(+m.name))
    def rule15(c):
        #if _PRINT:
            print('warn : {0}, risk : {1}'.format(warn_cnt(), risk_cnt()))

with ruleset('result'):
    @when_all(s.status == 'complete')
    def start(c):
        c.s.status = 'end'
        print('경고신호가 {0} 건 발생되었습니다.'.format(warn_cnt()))
        print('위험신호가 {0} 건 발생되었습니다.'.format(risk_cnt()))
        c.delete_state()
try:
    assert_fact('monitoring',{'name':'storeTank','type':'TYPE1','pressure':3})
except BaseException as e: print('Exception Message {0}'.format(e.message))
try:
    assert_fact('monitoring',{'name':'storeTank','type':'TYPE2','pressure':93})
except BaseException as e: print('Exception Message {0}'.format(e.message))
try:
    assert_fact('monitoring',{'name':'compressor','inPressure':90,'outPressure':100,'temperature':5})
except BaseException as e: print('Exception Message {0}'.format(e.message))
try:
    assert_fact('monitoring',{'name':'compressor','inPressure':9,'outPressure':90,'temperature':30})
except BaseException as e: print('Exception Message {0}'.format(e.message))
try:
    assert_fact('monitoring',{'name':'compressorGas','temperature':140,'pressure':9})
except BaseException as e: print('Exception Message {0}'.format(e.message))
try:
    assert_fact('monitoring',{'name':'detectGas','index':140,'detect':'Y'})
except BaseException as e: print('Exception Message {0}'.format(e.message))
try:
    assert_fact('monitoring',{'name':'detectFlame','index':140,'detect':'Y'})
except BaseException as e: print('Exception Message {0}'.format(e.message))
try:
    assert_fact('monitoring',{'name':'breaker','index':140,'detect':'Y'})
except BaseException as e: print('Exception Message {0}'.format(e.message))
try:
    assert_fact('monitoring',{'name':'operator','inOperate':'0','notOperate':'1'})
except BaseException as e: print('Exception Message {0}'.format(e.message))
try:
    assert_fact('monitoring',{'name':'freezer','temperature':'-30'})
except BaseException as e: print('Exception Message {0}'.format(e.message))

update_state('result',{'status':'complete'})