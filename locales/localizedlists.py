import re


class helper:
  acronyms_dic = {
    "de_DE" : {
      r"\bGRUNDST\b" : "Grundsteuer", "\bUSt[\.]{1,}" : "Umsatzsteuer", "\bMW[\-\.]{0,}St[\.]{1,}" : "Mehrwertsteuer",
      "MWST": "Mehrwertsteuer",# Switzerland
      r"\bFil[\.]{1,}" : "Filiale", "\behem[\.]{1,}" : "ehemalig",
      r"\bNts\b" : "Notes", r"\bAuftr[\-\.]{0,}Nr[\.]{0,}" : "Auftragsnummer",
      r"\bKd[\-\.]{0,}Nr[\.]{0,}" : "Kundennummer", r"\bRe[\-\.]{0,}Nr[\.]{0,}" : "Rechnungsnummer"
    },
    "en_GB" : {
      r"\bLtd" : "Limited", "VAT": "Value added tax", "\bReg[\-\.]{0,}\b": "Registration", "\bNo[\.]{1,}" : "Number"
    }
  }