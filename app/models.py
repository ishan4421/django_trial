from django.db import models

# Create your models here.

class Investor(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(unique = True)

    def __str__(self):
        return self.name
    
class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE, related_name="portfolios")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (Investor: {self.investor.name})"
    
class Stock(models.Model):
    ticker_symbol = models.CharField(max_length=10)
    company_name = models.CharField(max_length=100)
    market = models.CharField(max_length=50)

    def __str__(self):
        return self.ticker_symbol
    
class PortfolioStock(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    shares = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField()

    class Meta:
        unique_together = ('portfolio', 'stock')  # Ensures each stock is added only once per portfolio

    def __str__(self):
        return f"{self.portfolio.name} - {self.stock.ticker_symbol}"

# Adding the many-to-many relationship with 'through' option
Portfolio.stocks = models.ManyToManyField(Stock, through=PortfolioStock, related_name="portfolios")

#adding this commnt for practise