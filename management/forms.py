from django import forms


class RequestEventForm(forms.Form):
    local = forms.CharField(
        label="local",
        max_length=100,
        min_length=10,
        widget=forms.TextInput(attrs={"placeholder": "Local do evento"}),
    )
    cargo = forms.CharField(
        label="cargo",
        max_length=40,
        min_length=5,
        widget=forms.TextInput(attrs={"placeholder": "ex: Professor, Aluno"}),
    )
    nome = forms.CharField(
        label="nome",
        max_length=200,
        min_length=5,
        widget=forms.TextInput(attrs={"placeholder": "Nome do evento"}),
    )
    tipo = forms.CharField(
        label="tipo",
        max_length=200,
        min_length=5,
        widget=forms.TextInput(
            attrs={"placeholder": "ex: Comemorativo, Acadêmico, Tecnológico"}
        ),
    )
    descricao = forms.CharField(
        label="descricao", max_length=200, min_length=5, widget=forms.Textarea()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update(
                {
                    "class": "w-full border-gray-300 rounded-md shadow-sm "
                    + "focus:border-green-800 focus:ring-green-800"
                }
            )
