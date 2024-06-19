from app_tdd import CasinoSecurity, Visitor


class TestCasinoSecurity():
    def test_allow_adult_entrance(self):
        visitor = Visitor(18, 0.1, False)
        assert CasinoSecurity().check_visitor_adulthood(
            visitor.get_age()) is True

    def test_deny_children_entrance(self):
        visitor = Visitor(10, 0.0, True)
        assert CasinoSecurity().check_visitor_adulthood(
            visitor.get_age()) is False

    def test_deny_alcoholic_entrance(self):
        visitor = Visitor(40, 0.5, False)
        assert CasinoSecurity().check_visitor_soberity(
            visitor.get_promille()) is False

    def test_allow_sportsman_entrance(self):
        visitor = Visitor(25, 0.0, False)
        assert CasinoSecurity().check_visitor_soberity(
            visitor.get_promille()) is True

    def test_allow_richman_entrance(self):
        visitor = Visitor(35, 0.2, False)
        assert CasinoSecurity().check_visitor_bankruptcy(
            visitor.get_bankruptcy()) is False

    def test_deny_hobo_entrance(self):
        visitor = Visitor(20, 0.4, True)
        assert CasinoSecurity().check_visitor_bankruptcy(
            visitor.get_bankruptcy()) is True
