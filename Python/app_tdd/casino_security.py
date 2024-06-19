class CasinoSecurity:
    def check_visitor_adulthood(self, age):
        return age >= 18

    def check_visitor_soberity(self, promille):
        return promille <= 0.3

    def check_visitor_bankruptcy(self, bankruptcy):
        return bankruptcy
