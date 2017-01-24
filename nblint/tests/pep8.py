Code Cell 4 that starts with 'plt.scatter(X[:, 0], X[:, 1], c=y_pred, s=60, cmap='Paired')' has the following                       errors
 tmp.py:3:17: E127 continuation line over-indented for visual indent
tmp.py:3:80: E501 line too long (89 > 79 characters)
tmp.py:4:1: W391 blank line at end of file

Code Cell 6 that starts with 'X_new = pd.DataFrame(X)' has the following                       errors
 tmp.py:4:1: E265 block comment should start with '# '

Code Cell 7 that starts with 'X_train, X_test, y_train, y_test = tts(X_new, y, test_size=.2, random_state = 9840)' has the following                       errors
 tmp.py:1:76: E251 unexpected spaces around keyword / parameter equals
tmp.py:1:78: E251 unexpected spaces around keyword / parameter equals
tmp.py:1:80: E501 line too long (83 > 79 characters)

Code Cell 8 that starts with 'ypreds1 = lr(random_state=9840).fit(X_train[[0,1]], y_train).predict(X_test[[0,1]])' has the following                       errors
 tmp.py:1:47: E231 missing whitespace after ','
tmp.py:1:79: E231 missing whitespace after ','
tmp.py:1:80: E501 line too long (83 > 79 characters)

Code Cell 10 that starts with 'print (accuracy_score(ypreds1, y_test), accuracy_score(ypreds2, y_test))' has the following                       errors
 tmp.py:1:6: E211 whitespace before '('

