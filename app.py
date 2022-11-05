from flask import Flask, render_template, url_for, request,redirect
from models import app, Pet, db


@app.route('/')
def index():
    pets = Pet.query.all()
    return render_template('index.html', pets = pets)

@app.route('/addpet', methods =['GET', 'POST'])
def add_pet():
    if request.form:
        newpet = Pet(name= request.form['name'], age=request.form['age'], url= request.form['url'],
                     breed=request.form['breed'], color= request.form['color'], weight= request.form['weight'],
                     url_tag= request.form['alt'], spay= request.form['spay'], housetrained= request.form['housetrained'],
                     description= request.form['description'])
        db.session.add(newpet)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addpet.html')

@app.route('/edit/<id>', methods =['GET', 'POST'])
def edit_pet(id):
    pet = Pet.query.get(id)
    if request.form:
        pet.name = request.form['name']
        pet.age = request.form['age']
        pet.pet_type = request.form['pet_type']
        pet.url= request.form['url']
        pet.breed=request.form['breed']
        pet.color= request.form['color']
        pet.weight= request.form['weight'],
        pet.tag= request.form['url_tag']
        pet.spay= request.form['spay']
        pet.house_trained= request.form['housetrained']
        pet.description= request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editpet.html', pet = pet)

@app.route('/pet/<id>')
def pet(id):
    return render_template('pet.html')

@app.route('/delete/<id>')
def delete(id):
    pet = Pet.query.get(id)
    db.session.delete(pet)
    db.session.commit()
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error), 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')