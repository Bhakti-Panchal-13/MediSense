def home():
    if request.method == 'POST':
        use_voice = request.form.get('use_voice')  # Check if voice input was selected

        if use_voice:
            symptoms = recognize_symptoms()  # Use speech recognition
        else:
            symptoms = request.form.get('symptoms')  # Use manual input

            if not symptoms or symptoms.lower() == "symptoms":
                message = "Please either write symptoms or you have written misspelled symptoms"
                return render_template('index.html', message=message,symptoms=symptoms)