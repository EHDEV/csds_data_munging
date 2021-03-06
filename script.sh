awk sed 2013films.txt

cat -20 2013films.txt | grep "\||" | sed 's/\||/;/g; s/^;//g;' | awk -F ';' 'BEGIN {printf "movie_title, movie_production_house, director, genre, publisher"}{print $1, $2, $3, $5, $6}'


p == gsub('publisher=.*[\|]');

g == gsub('\]  .+<\w')

head -50 2013films.txt | grep "\||" | sed 's/\||/;/g; s/^;//g;' | awk -F ';' '{b=$4$5$6$7$8$910; print $1 ";" $2 ";" $3, ";", b}' | gawk -F ';' '{match($1, "[a-zA-Z0-9 ]+[\\w ]+[a-zA-Z 0-9 \\.]+", c1); match($4, "\]  .+<\\w", ca); match(ca[0], "\\w+", c4); match($4, "[^publisher=][a-zA-Z0-9]+[. \\w]+", c5); gsub(/[.]/,"", c5[0]);} {print $1 c1[0]}'

cat 2013films.txt | grep "\||" | sed 's/\||/;/g; s/^;//g;' | awk -F ';' '{b=$4$5$6$7$8$910; print $1 ";" $2 ";" $3, ";", b}' | gawk -F ';' '{match($1, "[a-zA-Z0-9 ]+[\\w ]+[a-zA-Z 0-9 \\.]+", c1); match($2, "[a-zA-Z0-9 ]+[\w ]+[a-zA-Z 0-9 \\.]+", c2); match($3, "[a-zA-Z0-9 ]+[\\w ]+[a-zA-Z 0-9 \\.]+", c3); match($4, "\\]  .+<\\w", ca); match(ca[0], "\\w+", c4); match($4, "publisher=.+\\|", cb); match(cb[0], "[^publisher=]\\w+[. \\w]+([. \\w]+)?", cd); match(cd[0], "[^\\.]+", c5)} {print c1[0], ";", c2[0], ";", c3[0], ";", c4[0], ";", c5[0]";"}' >> submit/awk_out.csv


\|[0-9{}][{ ]