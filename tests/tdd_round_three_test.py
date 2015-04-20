from source.AlertSystem import AlertSystem
from source.AlertSystem import Event
from source.Orc import *
from mock import patch
from unittest import TestCase
import random

def getRandomName():
    return 'Randy'

class TestEventId(TestCase):
    """
    When identifying threats I want each threat to
    have a unique id that so I can reference it to get more details
    """
    def testEventIdIncrement(self):
        # The event_count variable is shared across all files that use the class since it is static
        count = Event.event_count
        e = Event('test')
        e2 = Event('test2')
        self.assertEqual(e._id, count)
        self.assertEqual(e2._id, count + 1)
        pass

class TestGenerateList(TestCase):
    """
    When I want to demo the capabilities, I want to be able
    to generate a listing of randomly generated orcs over time
    so that we can better market the defense shield without needing to be under attack.
    """
    def testGenerateOrcList(self):

        height, width = 200, 200
        orcs = []
        for n in range(100):
            p0 = (random.randint(0, width), random.randint(0, height))
            p1 = (random.randint(0, width), random.randint(0, height))
            orcs.append(Orc(getRandomName(), p0, p1, 1))
        self.assertTrue(len(orcs) == 100)

        pass


class TestCheatCode(TestCase):
    """
    When I'm bored of an attack, I want to be able to type
    "ENTer the Trees" to get rid of all orcs so that I can always win.
    """
    @patch('source.AlertSystem.logging')
    def testCheat(self, mock_logging):
        self.assertFalse(mock_logging.info.called)
        alert_system = AlertSystem()
        self.assertTrue(mock_logging.info.called)
        alert_system.put(Event('ENTer the Trees'))
        self.assertTrue(mock_logging.info.called)
        pass



