from source.AlertSystem import AlertSystem
from source.AlertSystem import Event
from source.Orc import *
from unittest import TestCase


class TestOptionsDisplay(TestCase):
    """
    When interfacing with the system I want "?" to display my options so
    I can see all commands
    """
    def testOptionsDisplay(self):
        alert_system = AlertSystem()

        e = Event('?')
        alert_system.put(e)

        self.assertTrue(alert_system.options_displayed)
        pass


class TestOrcTypes(TestCase):
    """
    When identifying the threats I want to be able to
    identify specific orcs by type(8 types minimum)
    so I know what I'm up against
    """
    def testOrcBaseType(self):
        orc = Orc('Fred')
        self.assertIsInstance(orc, Orc().__class__)
        self.assertNotIsInstance(orc, OrcCommander().__class__)
        pass

    def testOrcRiderMedicFighterType(self):
        orc_fighter = OrcFighter('Todd')
        orc_medic = OrcMedic('Todd')
        orc_rider = OrcRider('Tom')

        self.assertIsInstance(orc_fighter, Orc().__class__)
        self.assertIsInstance(orc_fighter, OrcFighter().__class__)

        self.assertIsInstance(orc_medic, Orc().__class__)
        self.assertIsInstance(orc_medic, OrcMedic().__class__)

        self.assertIsInstance(orc_rider, Orc().__class__)
        self.assertIsInstance(orc_rider, OrcRider().__class__)
        pass

    def testOrcFighters(self):
        orc_fighter = OrcFighter('Todd')
        orc_grunt = OrcGrunt('Grunty')
        orc_kamakazi = OrcKamakazi('Angelo')
        orc_artillery = OrcArtillery('Art')

        self.assertIsInstance(orc_fighter, Orc().__class__)
        self.assertIsInstance(orc_fighter, OrcFighter().__class__)

        self.assertIsInstance(orc_grunt, Orc().__class__)
        self.assertIsInstance(orc_grunt, OrcFighter().__class__)
        self.assertIsInstance(orc_grunt, OrcGrunt().__class__)

        self.assertIsInstance(orc_kamakazi, Orc().__class__)
        self.assertIsInstance(orc_kamakazi, OrcFighter().__class__)
        self.assertIsInstance(orc_kamakazi, OrcKamakazi().__class__)

        self.assertIsInstance(orc_artillery, Orc().__class__)
        self.assertIsInstance(orc_artillery, OrcFighter().__class__)
        self.assertIsInstance(orc_artillery, OrcArtillery().__class__)
        pass

    def testOrcRiders(self):
        orc_rider = OrcRider('Todd')
        orc_commander = OrcCommander('Paul')
        orc_general = OrcGeneral('The General')

        self.assertIsInstance(orc_rider, Orc().__class__)
        self.assertIsInstance(orc_rider, OrcRider().__class__)

        self.assertIsInstance(orc_commander, Orc().__class__)
        self.assertIsInstance(orc_commander, OrcRider().__class__)
        self.assertIsInstance(orc_commander, OrcCommander().__class__)

        self.assertIsInstance(orc_general, Orc().__class__)
        self.assertIsInstance(orc_general, OrcRider().__class__)
        self.assertIsInstance(orc_general, OrcGeneral().__class__)

        pass


class TestAlertFilterId(TestCase):
    """
    When defending the kingdom I want a way to remove threats
    based on unique id, so I can focus on only the alive threats
    """
    def testAlertWithId(self):
        alert_sys = AlertSystem()
        Event('test', {'id': 4})
        Event('test', {'id': 3})

        alert_sys._log_dump(lambda e: e.id == 4)
        pass


class TestConfigurableUnits(TestCase):
    """
    When using the system I want to be able to identify
    units (imperial, metric, parsec or nautical) using a
    global setting so I can market this to other countries.
    """
    def testAllUnits(self):
        alert_sys = AlertSystem('imperial')
        Event('test', {'position': (0, 0), 'destination': (20, 10)})

        alert_sys = AlertSystem('metric')
        Event('test', {'position': (0, 0), 'destination': (20, 10)})

        alert_sys = AlertSystem('parsec')
        Event('test', {'position': (0, 0), 'destination': (20, 10)})

        alert_sys = AlertSystem('nautical')
        Event('test', {'position': (0, 0), 'destination': (20, 10)})


class TestOrcPriority(TestCase):
    """
    When analyzing threats I want to be able to set the priority of
    each orc so my troops know where to target
    """
    def testOrcAggro(self):
        start_pos = (0, 0)
        dest_pos = (10, 10)
        speed = 1
        aggro = 1  # higher aggro = higher threat = higher priority to target
        Event('low aggro orc', Orc('ned', start_pos, dest_pos, speed, aggro))
        pass