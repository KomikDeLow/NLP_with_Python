# fine
# Andrew Melnyk ALs-12

# You can modify the grammar in the recursive descent parser demo by selecting
# Edit Grammar in the Edit menu. Change the first expansion production, namely
# NP -> Det N PP,  to  NP -> NP PP. Using the Step button, try to build a parse tree.
# What happens?

# Answer:

# Відбувається зациклення програми на першому правилі.
# Воно є рекурсивним, тобто виражається само через себе,
# і тому аналізатор ніколи не перейде до наступного правила.
