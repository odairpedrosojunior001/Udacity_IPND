text="all zip files are zipped"
primeira_ocorrencia=text.find("zip")
segunda_ocorrencia=text.find("zip",primeira_ocorrencia+1)
print segunda_ocorrencia
