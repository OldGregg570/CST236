from source.AlertSystem import AlertSystem
from source.AlertSystem import Event
from source.Orc import Orc, OrcCommander
from unittest import TestCase


class TestAlertSystem(TestCase):
    def testBreached(self):
        """
        When defending against Orcs I want a way to tell
        when one has breached the perimeter so I can deploy defenses
        """
        alert_sys = AlertSystem()
        orc = Orc('charlie')
        e = Event('breach', orc)
        alert_sys.put(e)

        event = alert_sys.get()
        self.assertTrue(event._message == 'breach')
        self.assertTrue(event._source._name == 'charlie')
        self.assertIsNone(alert_sys.get())


class TestAlertFilters(TestCase):
    def testAlertFiltersOrc(self):
        """
        When diagnosing alert system issues, I want a way to isolate
        output from particular modules at certain levels so
        I don't have to sift through as much logging data
        """
        alert_sys = AlertSystem()
        orc_ted = OrcCommander('Teddy')
        orc_charlie = Orc('Charlie')

        alert_sys.put(Event('starting game', None, 'info'))

        event_a = Event('breach', orc_charlie, 'warning')
        alert_sys.put(event_a)

        event_b = Event('retreat', orc_ted, 'info')
        alert_sys.put(event_b)

        alert_sys._log_dump(lambda e: type(e) == Orc().__class__)

        self.assertIsNone(alert_sys.get())
        pass

    def testAlertFiltersOrcCommander(self):
        """
        When diagnosing alert system issues, I want a way to isolate
        output from particular modules at certain levels so
        I don't have to sift through as much logging data
        """
        alert_sys = AlertSystem()
        orc_ted = OrcCommander('Teddy')
        orc_charlie = Orc('Charlie')

        alert_sys.put(Event('starting game', None, 'info'))

        event_a = Event('breach', orc_charlie, 'warning')
        alert_sys.put(event_a)

        event_b = Event('retreat', orc_ted, 'info')
        alert_sys.put(event_b)

        alert_sys._log_dump(lambda e: type(e) == OrcCommander().__class__)

        self.assertIsNone(alert_sys.get())
        pass

    def testAlertNoFilters(self):
        """
        When diagnosing alert system issues, I want a way to isolate
        output from particular modules at certain levels so
        I don't have to sift through as much logging data
        """
        alert_sys = AlertSystem()
        orc_ted = Orc('Teddy')
        orc_charlie = Orc('Charlie')

        alert_sys.put(Event('starting game', None, 'info'))

        event_a = Event('breach', orc_charlie, 'warning')
        alert_sys.put(event_a)

        event_b = Event('retreat', orc_ted, 'info')
        alert_sys.put(event_b)

        alert_sys._log_dump()

        self.assertIsNone(alert_sys.get())
        pass


class TestAlertSystemAbort(TestCase):
    def testRageQuit(self):
        """
        When interfacing with the system I want "X" to quit
        the program so I can stop this charade.
        """
        alert_system = AlertSystem()
        orc_ted = Orc('Teddy')

        e = Event('X', orc_ted)
        alert_system.put(e)

        self.assertIsNone(alert_system.get())
        pass


class TestAlertSystemExtraInfo(TestCase):
    def testDistance(self):
        """
        When analyzing threats I want a way to see distance
        so I can tell how far away each one is.
        """
        orc_charlie = Orc('Charlie', (0, 0), (10, 10))

        self.assertAlmostEqual(orc_charlie.get_distance(), 14.14, 2)

        orc_teddy = Orc('Teddy', (0, 0), (2, 4))

        self.assertAlmostEqual(orc_teddy.get_distance(), 4.47, 2)


        pass

    def testVelocity(self):
        """
        When analyzing threats I want a way to see velocity so I can tell
        how quickly it's closing in.
        """
        pos = (0, 0)
        orc_charlie = Orc('Charlie', pos, (2, 2))
        orc_teddy = Orc('Teddy', pos, (1, 1))
        orc_marty = Orc('Marty', pos, (0, 1))
        orc_jimmy = Orc('Jimmy', pos, (1, 0.01))

        self.assertAlmostEqual(orc_charlie.get_velocity()[0], 0.707, 2)
        self.assertAlmostEqual(orc_charlie.get_velocity()[1], 0.707, 2)

        self.assertAlmostEqual(orc_teddy.get_velocity()[0], 0.707, 2)
        self.assertAlmostEqual(orc_teddy.get_velocity()[1], 0.707, 2)

        self.assertAlmostEqual(orc_marty.get_velocity()[0], 0.0, 2)
        self.assertAlmostEqual(orc_marty.get_velocity()[1], 1.0, 2)

        orc_marty = Orc('Marty', pos, (1, 0))

        self.assertAlmostEqual(orc_marty.get_velocity()[0], 1.0, 2)
        self.assertAlmostEqual(orc_marty.get_velocity()[1], 0.0, 2)

        self.assertAlmostEqual(orc_jimmy.get_velocity()[0], 0.999, 2)
        pass

