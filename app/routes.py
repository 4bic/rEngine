# import app
#
# from app import models
# from models import User,Keyword,Results
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# # Save name & e-mail to database and send to success page
# @app.route('/prereg', methods=['POST'])
# def prereg():
#     name = None
#     email = None
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         # Check that email does not already exist (not a great query, but works)
#         if not db.session.query(User).filter(User.email == email).count():
#             reg = User(name,email)
#             db.session.add(reg)
#             db.session.commit()
#             return render_template('success.html')
#     return render_template('index.html')
#
# #
# # @app.route('/keywords')
# # def word_entry():
# #     return render_template('wordy.html')
#
# @app.route('/word_search', methods=['POST'])
# def word_search():
#     search_term = None
#     if request.method == 'POST':
#         search_term = request.form['search_term']
#         if not db.session.query(Keyword).filter(Keyword.search_term == search_term).count():
#             reg = Keyword(search_term)
#             db.session.add(reg)
#             db.session.commit()
#         return render_template('results.html')
#     return render_template('wordy.html')
#
# @app.route('/results',)
# def search_results():
#     results = Results.query.all()
#
#     return render_template('results.html', results=results)
