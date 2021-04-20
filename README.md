# namer
Another random adjective-noun name generator; seeking names with punk poetry, the terms in the base list were hand-selected largely from band names, album titles, and beat generation writing. 

Alternatively, it also includes a list of words taken from ["The Turbo-Encabulator in Industry"](https://www.floobydust.com/turbo-encabulator/), first published by J. H. Quick of the Institution of Electrical Engineers in London, England in the Institution's _Students' Quarterly Journal_ vol 15 no. 58 p. 22 in December 1944. (The Turbo-Encabulator text was parsed with help from the exellent [spaCy](https://spacy.io/) NLP library.)

Suitable for use as either a [Google Cloud Function](https://cloud.google.com/functions/docs/quickstart-python):

```sh
gcloud functions deploy namer \
  --entry-point namer \
  --runtime python39 \
  --trigger-http \
  --allow-unauthenticated
```

or a  simple command line script:

```sh
python main.py --list=encabulator
```

Currently available at https://us-central1-whereami-map.cloudfunctions.net/namer

## Web API
- `GET` request to `/` returns one name as plain text
- Add `list=encabulator` to the request, either as JSON or query-string arguments, to get a name based on the Turbo-Encabulator terms
- (`list=namer` also works to get the original list, but is not required)
- There are no other methods or endpoints

## CLI

`main.py` uses only standard library, so you should be able invoke `main.py` directly. It will default to the original `namer` list, or you can pass it `(--list|-l)=encabulator` to get a name based on Turboencabulator terms.
