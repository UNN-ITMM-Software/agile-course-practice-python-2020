## **Debt servicing expenses**

*  D – required sum
*  Y – payment
*  I – percent
*  R – expenses
*  g – percent rate
*  n – period

**Formula:**

Y = I + R
I = D * g

### Equal amounts repayment:

R = D / n

Yt = D t-1 * g + R, t = 1..n

    # Example.
    # D = 200 000, g = 14%, n = 4.

    # R = 200000 / 4 = 50000
    # percent_for_year = 200000 • 0,14 = 28 000 ; (200000 - 50000) - 0,14 = 21 000 ; etc
    # 1 year - payment = 78000 expenses = 50000
    # 2 year - payment = 71000 expenses = 50000
    # 3 year - payment = 64000 expenses = 50000
    # 4 year - payment = 57000 expenses = 50000

### Equal payments repayment:

Y =  D t-1 * g + R t = const

Y = D / convertion_rate

Rt = R t-1 (1 + g)

    # Example.
    # D = 200 000, g = 14%, n = 4.

    # convertion_rate = (1 - (1 + 0,14)^(-4)) / 0,14 = 2,913712
    # Y = D / convertion_rate = 68641
    # percent_for_year = 200000 • 0,14 = 28 000 ; (200000 - 50000) - 0,14 = 21 000 ; etc
    # 1 year - payment = 68641 expenses = 40641
    # 2 year - payment = 68641 expenses = 46330
    # 3 year - payment = 68641 expenses = 52817
    # 4 year - payment = 68641 expenses = 60212
