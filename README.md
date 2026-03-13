# Επαγωγική Στατιστική και Ανάλυση Δεδομένων
## Κώδικας Υλοποίησης σε R και Python

Αυτό το repository περιέχει όλες τις υλοποιήσεις σε **R** και **Python** που συνοδεύουν το βιβλίο  
*«Επαγωγική Στατιστική και Ανάλυση Δεδομένων»*.

Κάθε αρχείο αντιστοιχεί σε ένα παράδειγμα του βιβλίου και ακολουθεί τη σύμβαση ονοματοδοσίας:

```
ChapterN/R/ExampleM.R    ←  υλοποίηση σε R
ChapterN/Python/ExampleM.py   ←  υλοποίηση σε Python
```

---

## Απαιτήσεις

### R
- **R** ≥ 4.0 — [https://cran.r-project.org](https://cran.r-project.org)
- **RStudio** (προαιρετικό αλλά συνιστάται) — [https://posit.co/download/rstudio-desktop](https://posit.co/download/rstudio-desktop)

Εγκατάσταση πακέτων:
```r
install.packages(c("ggplot2", "dplyr", "car", "pwr", "emmeans",
                   "multcomp", "agricolae", "gridExtra"))
```

### Python
- **Python** ≥ 3.9 — [https://www.python.org](https://www.python.org)

Εγκατάσταση βιβλιοθηκών:
```bash
pip install numpy pandas matplotlib seaborn scipy statsmodels
```

---

## Μέρος Ι — Θεμελιώδεις Έννοιες

### Κεφάλαιο 1 — Εισαγωγή στην Επαγωγική Στατιστική

| Αρχείο | Περιεχόμενο |
|--------|-------------|
| `Chapter1/R/Example1.R` / `Chapter1/Python/Example1.py` | Βασικές πράξεις, δημιουργία και χειρισμός δεδομένων (vectors, data frames), βασικά γραφήματα (histogram, boxplot, line plot) |

### Κεφάλαιο 2 — Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες

| Αρχείο | Περιεχόμενο |
|--------|-------------|
| `Chapter2/R/Example1.R` / `Chapter2/Python/Example1.py` | Υπολογισμοί διακριτής κατανομής: αναμενόμενη τιμή, διακύμανση, τυπική απόκλιση, γράφημα κατανομής πιθανοτήτων |
| `Chapter2/R/Example2.R` / `Chapter2/Python/Example2.py` | Προσομοίωση θεωρήματος Bayes με Monte Carlo: τρία εργοστάσια, πιθανότητα ελαττωματικού ανά εργοστάσιο (100.000 επαναλήψεις) |
| `Chapter2/R/Example3.R` / `Chapter2/Python/Example3.py` | Ανάλυση χαρτοφυλακίου δύο μετοχών (A: 8%/15%, B: 12%/20%), βάρη 60/40, μέση απόδοση, τυπική απόκλιση, συσχέτιση |

---

## Μέρος ΙΙ — Διακριτές Κατανομές

### Κεφάλαιο 3 — Διωνυμική Κατανομή

| Αρχείο | Περιεχόμενο |
|--------|-------------|
| `Chapter3/R/Example1.R` / `Chapter3/Python/Example1.py` | Βασικοί υπολογισμοί για B(10, 0.3): P(X=3), P(X≤5), P(X≥4) |
| `Chapter3/R/Example2.R` / `Chapter3/Python/Example2.py` | Ποιοτικός έλεγχος — δειγματοληψία αποδοχής (n=100, c=3): πιθανότητες για p=2% και p=5% |
| `Chapter3/R/Example3.R` / `Chapter3/Python/Example3.py` | Οπτικοποίηση B(20, 0.4): ραβδόγραμμα PMF, σήμανση μέσης τιμής |
| `Chapter3/R/Example4.R` / `Chapter3/Python/Example4.py` | Προσομοίωση B(50, 0.3) με 1.000 επαναλήψεις: σύγκριση με θεωρητική κατανομή |
| `Chapter3/R/Example5.R` / `Chapter3/Python/Example5.py` | Σύγκριση B(20, p) για p=0.2, 0.5, 0.8: τέσσερα γραφήματα (3 επιμέρους + overlay) |
| `Chapter3/R/Example6.R` / `Chapter3/Python/Example6.py` | Ικανοποίηση πελατών B(20, 0.65): P(A), P(B), P(A∩B), P(A∪B), δεσμευμένη P(A|B) |
| `Chapter3/R/Example7.R` / `Chapter3/Python/Example7.py` | Δύο γραμμές παραγωγής A~B(50,0.08) και B~B(60,0.05): αναμενόμενα ελαττωματικά, σύγκριση |

### Κεφάλαιο 4 — Κατανομή Poisson

| Αρχείο | Περιεχόμενο |
|--------|-------------|
| `Chapter4/R/Example1.R` / `Chapter4/Python/Example1.py` | Βασικοί υπολογισμοί για Poisson(5): P(X=4), P(X≤6), P(X≥3) |
| `Chapter4/R/Example2.R` / `Chapter4/Python/Example2.py` | Call center Poisson(30): P(X=25), P(X>35), 95ο εκατοστημόριο |
| `Chapter4/R/Example3.R` / `Chapter4/Python/Example3.py` | Οπτικοποίηση Poisson(7): ραβδόγραμμα PMF, σήμανση λ |
| `Chapter4/R/Example4.R` / `Chapter4/Python/Example4.py` | Προσομοίωση Poisson(6) με 1.000 παρατηρήσεις: ιστόγραμμα vs θεωρητική κατανομή |
| `Chapter4/R/Example5.R` / `Chapter4/Python/Example5.py` | Σύγκριση Poisson(λ) για λ=2, 5, 10: τέσσερα γραφήματα |
| `Chapter4/R/Example6.R` / `Chapter4/Python/Example6.py` | Προσέγγιση Poisson της Διωνυμικής: B(100, 0.03) ≈ Poisson(3), μέγιστη απόλυτη διαφορά |
| `Chapter4/R/Example7.R` / `Chapter4/Python/Example7.py` | Ασφαλιστική εταιρεία Poisson(3): P(X>5), 95% CI, πίνακας πιθανοτήτων |
| `Chapter4/R/Example8.R` / `Chapter4/Python/Example8.py` | X~Poisson(4), Y~Poisson(6): X+Y~Poisson(10), δεσμευμένη P(Tech=3|Total=8) |
| `Chapter4/R/Example9.R` / `Chapter4/Python/Example9.py` | Τρεις γραμμές Poisson(2/3/5) με βάρη 30/45/25%: Bayes P(C|X=4), Poisson–Διωνυμική |

### Κεφάλαιο 5 — Άλλες Διακριτές Κατανομές

| Αρχείο | Περιεχόμενο |
|--------|-------------|
| `Chapter5/R/Example1.R` / `Chapter5/Python/Example1.py` | Γεωμετρική p=0.3: P(X=5), P(X≤4), P(X>6) — διαφορά κωδικοποίησης R vs Python |
| `Chapter5/R/Example2.R` / `Chapter5/Python/Example2.py` | Υπεργεωμετρική N=100, K=15, n=20: P(X=3), P(X≤2), αναμενόμενος αριθμός ελαττωματικών |
| `Chapter5/R/Example3.R` / `Chapter5/Python/Example3.py` | Αρνητική Διωνυμική r=5, p=0.4: P(X=12), αναμενόμενος αριθμός δοκιμών, διακύμανση |
| `Chapter5/R/Example4.R` / `Chapter5/Python/Example4.py` | Υπεργεωμετρική vs Διωνυμική N=100, K=30, n=20: γράφημα σύγκρισης |
| `Chapter5/R/Example5.R` / `Chapter5/Python/Example5.py` | Προσομοίωση Γεωμετρικής p=0.2 με 1.000 παρατηρήσεις: ιστόγραμμα vs θεωρητική |

---

## Μέρος ΙΙΙ — Συνεχείς Κατανομές

### Κεφάλαιο 6 — Κανονική Κατανομή

| Αρχείο | Περιεχόμενο |
|--------|-------------|
| `Chapter6/R/Example1.R` / `Chapter6/Python/Example1.py` | Βασικοί υπολογισμοί για X~N(100,15²): P(X≤120), P(X>90), P(85<X<110) |
| `Chapter6/R/Example2.R` / `Chapter6/Python/Example2.py` | Κβαντίλια για X~N(50,10²): Q1, Q2, Q3, IQR |
| `Chapter6/R/Example3.R` / `Chapter6/Python/Example3.py` | Οπτικοποίηση N(70,12²): καμπύλη PDF, σήμανση ±1σ (68%) και ±2σ (95%) |
| `Chapter6/R/Example4.R` / `Chapter6/Python/Example4.py` | Προσομοίωση N(100,15²) με n=10.000: επαλήθευση εμπειρικού κανόνα 68-95-99.7% |
| `Chapter6/R/Example5.R` / `Chapter6/Python/Example5.py` | Σύγκριση N(50,5²), N(50,10²), N(60,5²): επίδραση μέσης τιμής και τυπικής απόκλισης |
| `Chapter6/R/Example6.R` / `Chapter6/Python/Example6.py` | Quality Control N(25,0.5²): ποσοστό εντός [24,26]mm, δείκτης ικανότητας Cp |

### Κεφάλαιο 7 — Τυπική Κανονική Κατανομή

| Αρχείο | Περιεχόμενο |
|--------|-------------|
| `Chapter7/R/Example1.R` / `Chapter7/Python/Example1.py` | Βασικοί υπολογισμοί για Z~N(0,1): P(Z≤1.5), P(Z>-0.8), P(-1<Z<2) |
| `Chapter7/R/Example2.R` / `Chapter7/Python/Example2.py` | Τυποποίηση X~N(100,15²): z-score για X=120, 90ο εκατοστημόριο με δύο τρόπους |
| `Chapter7/R/Example3.R` / `Chapter7/Python/Example3.py` | Οπτικοποίηση Z~N(0,1): κρίσιμες τιμές ±1.96 (95%) και ±1 (68%), σκίαση 95% |
| `Chapter7/R/Example4.R` / `Chapter7/Python/Example4.py` | Ακριβής επαλήθευση: P(±1σ)=68.27%, P(±2σ)=95.45%, P(±3σ)=99.73% |
| `Chapter7/R/Example5.R` / `Chapter7/Python/Example5.py` | Πωλήσεις X~N(50.000,8.000²): πιθανότητες ανά κατηγορία, κβαντίλια 10ο–95ο |

### Κεφάλαιο 8 — Άλλες Σημαντικές Συνεχείς Κατανομές

| Αρχείο | Περιεχόμενο |
|--------|-------------|
| `Chapter8/R/Example1.R` / `Chapter8/Python/Example1.py` | Ομοιόμορφη U(5,15): P(X≤10), P(8<X<12), 75ο εκατοστημόριο |
| `Chapter8/R/Example2.R` / `Chapter8/Python/Example2.py` | Εκθετική Exp(λ=0.5): P(X≤2), P(X>3), διάμεσος, μέση τιμή |
| `Chapter8/R/Example3.R` / `Chapter8/Python/Example3.py` | t-Student t(10): P(T≤1.5), P(-2<T<2), κρίσιμη τιμή, σύγκριση με N(0,1) |
| `Chapter8/R/Example4.R` / `Chapter8/Python/Example4.py` | χ²(10) και F(5,10): κρίσιμες τιμές α=5%, περιοχές απόρριψης |
| `Chapter8/R/Example5.R` / `Chapter8/Python/Example5.py` | Σύγκριση t(3), t(10), t(30) vs N(0,1): σύγκλιση προς κανονική |
| `Chapter8/R/Example6.R` / `Chapter8/Python/Example6.py` | Σύγκριση χ²(2), χ²(5), χ²(10), χ²(15): σχέση βαθμών ελευθερίας με μ και σ² |
| `Chapter8/R/Example7.R` / `Chapter8/Python/Example7.py` | F(19,24): σύγκριση μεταβλητότητας δύο καταστημάτων, αμφίπλευρος F-test |

---

## Μέρος ΙV — Δειγματοληπτικές Κατανομές

### Κεφάλαιο 9 — Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες

| Αρχείο | Περιεχόμενο |
|--------|-------------|
| `Chapter9/R/Example1.R` / `Chapter9/Python/Example1.py` | Δειγματικά στατιστικά μισθών: n, x̄, s², s, διάμεσος |
| `Chapter9/R/Example2.R` / `Chapter9/Python/Example2.py` | Απλή τυχαία δειγματοληψία N=500, n=50: στατιστικά ανά τμήμα |
| `Chapter9/R/Example3.R` / `Chapter9/Python/Example3.py` | Αναλογική στρωματοποιημένη δειγματοληψία N=1000, 4 τμήματα, n=100 |
| `Chapter9/R/Example4.R` / `Chapter9/Python/Example4.py` | Δειγματοληψία κατά συστάδες N=5000, 50 καταστήματα, επιλογή 5 |
| `Chapter9/R/Example5.R` / `Chapter9/Python/Example5.py` | Προσομοίωση δειγματοληπτικού σφάλματος: N=10000, 1000 δείγματα n=30 |
| `Chapter9/R/Example6.R` / `Chapter9/Python/Example6.py` | Επίδραση μεγέθους δείγματος στο SE: SE=σ/√n για n∈{10,30,50,100,200,500} |
| `Chapter9/R/Example7.R` / `Chapter9/Python/Example7.py` | Δειγματοληπτική κατανομή με ζάρι {1..6}: n=2, 10000 επαναλήψεις, E[x̄]=μ |
| `Chapter9/R/Example8.R` / `Chapter9/Python/Example8.py` | Στρωματοποιημένη δειγματοληψία ελέγχου ποιότητας: 3 γραμμές, Monte Carlo 1000 επαναλήψεων |
| `Chapter9/R/Example9.R` / `Chapter9/Python/Example9.py` | Cluster vs Stratified: 80 καταστήματα, 4 περιφέρειες — λόγος διακύμανσης |
| `Chapter9/R/Example10.R` / `Chapter9/Python/Example10.py` | Μεροληψία μη απόκρισης: εκτίμαση με στάθμιση αντίστροφης πιθανότητας (IPW) |
| `Chapter9/R/Example11.R` / `Chapter9/Python/Example11.py` | Σχεδιασμός δημοσκόπησης N=50000: n για ±3% MoE, SRS vs Stratified vs Systematic |

### Κεφάλαιο 10 — Δειγματοληπτικές Κατανομές και Κεντρικό Οριακό Θεώρημα

| Αρχείο | Περιεχόμενο |
|--------|-------------|
| `Chapter10/R/Example1.R` / `Chapter10/Python/Example1.py` | ΚΟΘ με U(0,10): ιστόγραμμα x̄ για n=5,10,30,100 με θεωρητική N(μ, σ²/n) |
| `Chapter10/R/Example2.R` / `Chapter10/Python/Example2.py` | ΚΟΘ με Exp(λ=0.5): σύγκλιση από ασύμμετρη κατανομή — 2×3 layout |
| `Chapter10/R/Example3.R` / `Chapter10/Python/Example3.py` | Q-Q plots για 4 κατανομές (Uniform, Exp, χ²(3), Normal), n=30 |
| `Chapter10/R/Example4.R` / `Chapter10/Python/Example4.py` | Εμπειρικό vs θεωρητικό SE: N(100,20), n=5..200, 1000 προσομοιώσεις |
| `Chapter10/R/Example5.R` / `Chapter10/Python/Example5.py` | Δειγματοληπτική κατανομή αναλογίας p=0.3: n=20,50,100,500 |
| `Chapter10/R/Example6.R` / `Chapter10/Python/Example6.py` | Ρυθμός σύγκλισης ΚΟΘ: Shapiro-Wilk × 4 κατανομές × 5 μεγέθη δείγματος — heatmap |

---

## Μέρος V — Στατιστική Συμπερασματολογία

### Κεφάλαιο 11 — Σημειακή Εκτίμηση

| Αρχείο | Περιγραφή |
|--------|-----------|
| `Chapter11/R/Example1.R` / `Chapter11/Python/Example1.py` | Βασικοί εκτιμητές: x̄, S², σ̂²_MLE, SE(x̄) — N(100,15²), n=50 |
| `Chapter11/R/Example2.R` / `Chapter11/Python/Example2.py` | Εκτίμηση αναλογίας: p̂, SE(p̂), Var(p̂) — n=400, x=340 |
| `Chapter11/R/Example3.R` / `Chapter11/Python/Example3.py` | MLE εκθετικής κατανομής: λ̂=1/x̄, οπτικοποίηση log-likelihood |
| `Chapter11/R/Example4.R` / `Chapter11/Python/Example4.py` | Monte Carlo σύγκριση S² vs MLE: Bias, Var, MSE — 10000 προσομοιώσεις |
| `Chapter11/R/Example5.R` / `Chapter11/Python/Example5.py` | Ανάλυση δεδομένων πωλήσεων: μέσος, διάμεσος, SD, CV, τεταρτημόρια |

### Κεφάλαιο 12 — Διαστήματα Εμπιστοσύνης

| Αρχείο | Περιγραφή |
|--------|-----------|
| `Chapter12/R/Example1.R` / `Chapter12/Python/Example1.py` | CI για μέση τιμή (γνωστό σ): z-interval, n=64, x̄=520, σ=80 |
| `Chapter12/R/Example2.R` / `Chapter12/Python/Example2.py` | CI για μέση τιμή (άγνωστο σ): t-interval, n=25 δεδομένα παραγωγής |
| `Chapter12/R/Example3.R` / `Chapter12/Python/Example3.py` | CI για διαφορά μέσων (ίσες διασπορές): pooled t, n1=20 vs n2=25 |
| `Chapter12/R/Example4.R` / `Chapter12/Python/Example4.py` | CI για διαφορά μέσων (άνισες διασπορές): Welch + F-test, 2 εργοστάσια |
| `Chapter12/R/Example5.R` / `Chapter12/Python/Example5.py` | CI για συζευγμένα δείγματα: paired t, βάρος πριν/μετά, n=15 |
| `Chapter12/R/Example6.R` / `Chapter12/Python/Example6.py` | CI για αναλογία: κανονική προσέγγιση, n=400, x=340 |
| `Chapter12/R/Example7.R` / `Chapter12/Python/Example7.py` | CI για διασπορά/SD: χ²-κατανομή, n=20 μετρήσεις (mm) |
| `Chapter12/R/Example8.R` / `Chapter12/Python/Example8.py` | Προσδιορισμός μεγέθους δείγματος: για μέσο και αναλογία, πίνακας n |
| `Chapter12/R/Example9.R` / `Chapter12/Python/Example9.py` | Οπτικοποίηση CI: Monte Carlo coverage, 100 CIs από N(100,15) |

### Κεφάλαιο 13 — Έλεγχοι Υποθέσεων

| Αρχείο | Περιγραφή |
|--------|-----------|
| `Chapter13/R/Example1.R` / `Chapter13/Python/Example1.py` | Έλεγχοι Z και t για μία μέση τιμή: H0:μ=8.0, n=25, Cohen's d, CI, ανάλυση ισχύος |
| `Chapter13/R/Example2.R` / `Chapter13/Python/Example2.py` | Έλεγχος αναλογίας: H0:p=0.80, n=500, x=380, Cohen's h, prop.test, μέγεθος δείγματος |
| `Chapter13/R/Example3.R` / `Chapter13/Python/Example3.py` | Έλεγχος διασποράς: H0:σ²=0.04, n=20, χ²-test, CI για σ² και σ, ισοδυναμία CI–test |
| `Chapter13/R/Example4.R` / `Chapter13/Python/Example4.py` | Οπτικοποίηση p-value: κατανομή t, κρίσιμες περιοχές, p-value ως εμβαδόν ουρών |
| `Chapter13/R/Example5.R` / `Chapter13/Python/Example5.py` | Σφάλματα τύπου I & II: οπτικοποίηση α, β, ισχύς, καμπύλες ισχύος, αμφίπλευρος vs μονόπλευρος |

### Κεφάλαιο 14 — Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA

| Αρχείο | Περιγραφή |
|--------|-----------|
| `Chapter14/R/Example1.R` / `Chapter14/Python/Example1.py` | Welch t-test δύο ανεξάρτητων δειγμάτων: n1=30, n2=25, F-test, Welch-Satterthwaite df, Cohen's d |
| `Chapter14/R/Example2.R` / `Chapter14/Python/Example2.py` | Paired t-test: n=12 ζεύγη βάρους πριν/μετά, μονόπλευρος, Shapiro-Wilk, γραφική ανά άτομο |
| `Chapter14/R/Example3.R` / `Chapter14/Python/Example3.py` | Σύγκριση δύο αναλογιών: n1=200, n2=220, pooled SE, prop.test/proportions_ztest, 95% CI |
| `Chapter14/R/Example4.R` / `Chapter14/Python/Example4.py` | Σύγκριση δύο διασπορών: F-test, Levene, κρίσιμες τιμές, n1=25 vs n2=30 |
| `Chapter14/R/Example5.R` / `Chapter14/Python/Example5.py` | One-Way ANOVA πλήρης: 3 στρατηγικές διαφήμισης, ANOVA table, eta², omega² |
| `Chapter14/R/Example6.R` / `Chapter14/Python/Example6.py` | Κανονικότητα υπολοίπων ANOVA: Shapiro-Wilk ανά ομάδα και συνολικά, Q-Q plot |
| `Chapter14/R/Example7.R` / `Chapter14/Python/Example7.py` | Ομοσκεδαστικότητα ANOVA: Levene, Bartlett, max/min variance ratio |
| `Chapter14/R/Example8.R` / `Chapter14/Python/Example8.py` | Εναλλακτικές μέθοδοι: Welch's ANOVA, Kruskal-Wallis, log-μετασχηματισμός |
| `Chapter14/R/Example9.R` / `Chapter14/Python/Example9.py` | Post-hoc αναλύσεις: Tukey HSD, Bonferroni, Scheffé, compact letter display |
| `Chapter14/R/Example10.R` / `Chapter14/Python/Example10.py` | Πλήρης ανάλυση δύο δειγμάτων: Z-test (γνωστό σ), Welch, pooled, Cohen's d, καμπύλη ισχύος |
| `Chapter14/R/Example11.R` / `Chapter14/Python/Example11.py` | Πλήρης ANOVA με post-hoc: 3 μέθοδοι διδασκαλίας, έλεγχοι παραδοχών, Tukey, Bonferroni |
| `Chapter14/R/Example12.R` / `Chapter14/Python/Example12.py` | Κλινική μελέτη: paired t-test (n=20 ζεύγη), σύγκριση αναλογιών, Cohen's h, γραφικά |

---

## Σημειώσεις για τη Χρήση

### Διαφορές R vs Python στις Κατανομές

| Κατανομή | R | Python (scipy) |
|----------|---|----------------|
| Γεωμετρική | `dgeom(x, p)` — μετράει **αποτυχίες** πριν την 1η επιτυχία | `geom.pmf(k, p)` — μετράει **δοκιμές** (k ≥ 1) |
| Υπεργεωμετρική | `dhyper(x, m, n, k)` — m=επιτυχίες, n=αποτυχίες | `hypergeom.pmf(k, M, n, N)` — M=πληθυσμός, n=επιτυχίες |
| Αρνητική Διωνυμική | `dnbinom(x, size, prob)` — μετράει **αποτυχίες** | `nbinom.pmf(k, n, p)` — μετράει **αποτυχίες** |
| Εκθετική | `dexp(x, rate=λ)` | `expon(scale=1/λ)` — scale είναι η **μέση τιμή** |
| Ομοιόμορφη | `dunif(x, min=a, max=b)` | `uniform(loc=a, scale=b-a)` |

### Αναπαραγωγιμότητα
Όλα τα παραδείγματα με προσομοίωση χρησιμοποιούν σταθερό seed:
- **R**: `set.seed(42)` ή `set.seed(123)`
- **Python**: `np.random.seed(42)` ή `np.random.seed(123)`

---

## Άδεια Χρήσης

© [2026] [Εκδόσεις ΚΡΙΤΙΚΗ]. Με επιφύλαξη παντός δικαιώματος.
Ο κώδικας αυτός αποτελεί αναπόσπαστο τμήμα του βιβλίου «Επαγωγική Στατιστική και Ανάλυση Δεδομένων» και διατίθεται αποκλειστικά για προσωπική εκπαιδευτική χρήση από κατόχους αντιτύπου του βιβλίου.
Απαγορεύεται ρητά:

- η αναδημοσίευση, αναδιανομή ή κοινοποίηση σε τρίτους
- η ενσωμάτωση σε άλλα έργα, εκπαιδευτικό υλικό ή λογισμικό
- οποιαδήποτε εμπορική χρήση
