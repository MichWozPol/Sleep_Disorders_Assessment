# Sleep_Disorders_Assessment

## About project
Flask survey app based on the architectural MVC pattern: <br>
<ul>
  <li>controller in our project is route file</li>
  <li>view refers to templates, which purpose are to render page (they contain static data as well as placeholders for dynamic data. A template is rendered with specific data to produce a final document)</li>
  <li>model is basically mutliple data structures taken from out database via SQLAlchemy library</li>
</ul>

## Fronted
Application consists of few HTML templates - base, index, about, route and also blueprints templates, created in purpose to catch peculiar errors - 403, 404 and 500.
Most templates extend from base template, in which there's a declaration of navbar and general website appearance.
Technologies used in frontend part:
<ul>
  <li> HTML </li>
  <li> CSS </li>
  <li> Bootstrap </li>
</ul>

## Backend
Backend part of project is heavily based on the MySQL database, which has tables like user, answer, vote and question.
Naturally different tables are properly connected with one another.
Moreover, user table has such restriction as IP address, which prevents user with fixed IP address to fill in the questionnaire more the once.
Besides, database has ON UPDATE and ON DELETE clauses, which are very convienient way to delete or update records in multiple tables at once.

## Results
To preprocess collected data and transform them into desired form we've created simple python script, available in the tools directory.
Afterwards we've analysed data using WEKA software (apriori WEKA files are available in the tools directory), U Mann-Whitney test and classifiers
such as CART, KNN and naive Bayes classifier (also accesible in the tools dir). The results are displayed on the "results" subpage.
