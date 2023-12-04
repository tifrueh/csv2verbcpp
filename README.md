# csv2verbcpp

This small python utility can be used to create .verb.cpp files to use in the development of [Conjugateur](https://github.com/tifrueh/conjugateur) from a specifically formatted CSV file.

## CSV specification

The utility reads the CSV with a Python csv.DictReader, which maps the information in each row to a dictionary which uses the values first row of the CSV file as keys. Therefore, the first line of the CSV always needs to be:

text
~~~
"Identifier","Infinitif","Participe présent","Type","Présent - je","Présent - tu","Présent - il","Présent - elle","Présent - nous","Présent - vous","Présent - ils","Présent - elles","Imparfait - je","Imparfait - tu","Imparfait - il","Imparfait - elle","Imparfait - nous","Imparfait - vous","Imparfait - ils","Imparfait - elles","Futur - je","Futur - tu","Futur - il","Futur - elle","Futur - nous","Futur - vous","Futur - ils","Futur - elles","Passé composé - je","Passé composé - tu","Passé composé - il","Passé composé - elle","Passé composé - nous","Passé composé - vous","Passé composé - ils","Passé composé - elles","Plus-que-parfait - je","Plus-que-parfait - tu","Plus-que-parfait - il","Plus-que-parfait - elle","Plus-que-parfait - nous","Plus-que-parfait - vous","Plus-que-parfait - ils","Plus-que-parfait - elles","Subjonctif - je","Subjonctif - tu","Subjonctif - il","Subjonctif - elle","Subjonctif - nous","Subjonctif - vous","Subjonctif - ils","Subjonctif - elles","Conditionnel - je","Conditionnel - tu","Conditionnel - il","Conditionnel - elle","Conditionnel - nous","Conditionnel - vous","Conditionnel - ils","Conditionnel - elles"
~~~

All the other rows should contain all the forms of a verb, beginning with the `Identifier`, continuing with the `Infinitif`, the `Participe présent`, etc.

See [template.csv](https://github.com/tifrueh/csv2verbcpp/blob/main/template.csv) for an example.
