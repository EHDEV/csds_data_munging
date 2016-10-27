


#cat worldcup.txt | sed 's/\[\[\([0-9]*\)[^]]*\]\]/\1/g; s/.*fb|\([A-Za-z]*\)}}/\1/g; s/<sup><\/sup>//g; s/|bgcolor[^|]*//g; s/|align=center[^|]*//g' | sed 's/\|[0-9 ][- 0-9]//'  | sed 's/(//' | sed 's/)//' | sed "s/\:.*//" | 

#awk 'BEGIN { RS = "|-" } ; { n = split($4,splt,"\n"); for (x = 0; x < n; x++) }{ match(splt[x], "\\w+", c4); if (length(tmp) > 0) print tmp[x];} ;{ }' 


# Final working line
cat worldcup.txt | sed 's/\[\[\([0-9]*\)[^]]*\]\]/\1/g; s/.*fb|\([A-Za-z]*\)}}/\1/g; s/<sup><\/sup>//g; s/|bgcolor[^|]*//g; s/|align=center[^|]*//g;s/\|[0-9 ][- 0-9]//;s/(//; s/)//; s/\:.*$//; s/^!.*//; s/^[[:alpha:]]/::&/g;' | sed '/|[0-9]/d' | sed '$d' | sed '$d' | sed '$d' | awk 'BEGIN { NR < 3; RS = "::" } ; { n = split($0,splt,"\\n"); } ;  { tmp=match(splt[1], /[A-Z]+/); rank = 0; { for (j=2; j<=5; j++) { n = split(splt[j], ln, ","); for (k = 1; k <= n; k++) { print splt[1], ",", ln[k], ",", j-1;  } } } }' | sed '/| —/d' | sed '/|-/d' > ./submit/awk_sed_worldcup_out.csv
