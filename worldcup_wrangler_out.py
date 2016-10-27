from wrangler import dw
import sys

if(len(sys.argv) < 3):
  sys.exit('Error: Please include an input and output file.  Example python script.py input.csv output.csv')

w = dw.DataWrangler()

# Cut  on '"'
w.add(dw.Cut(column=[],
             table=0,
             status="active",
             drop=False,
             result="column",
             update=True,
             insert_position="right",
             row=None,
             on="\"",
             before=None,
             after=None,
             ignore_between=None,
             which=1,
             max=0,
             positions=None))

# Split data repeatedly on '|\{'  into  rows
w.add(dw.Split(column=["data"],
               table=0,
               status="active",
               drop=True,
               result="row",
               update=False,
               insert_position="right",
               row=None,
               on="\\|\\{",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max="0",
               positions=None,
               quote_character=None))

# Split data repeatedly on '(align=||[0-9] )'
w.add(dw.Split(column=["data"],
               table=0,
               status="active",
               drop=True,
               result="column",
               update=False,
               insert_position="right",
               row=None,
               on="(align=|\\|[0-9] )",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max="0",
               positions=None,
               quote_character=None))

# Delete row 1
w.add(dw.Filter(column=[],
                table=0,
                status="active",
                drop=False,
                row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.RowIndex(column=[],
                  table=0,
                  status="active",
                  drop=False,
                  indices=[0])])))

# Set  split1  name to  1
w.add(dw.SetName(column=["split1"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["1"],
                 header_row=None))

# Set  split2  name to  2
w.add(dw.SetName(column=["split2"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["2"],
                 header_row=None))

# Set  split3  name to  3
w.add(dw.SetName(column=["split3"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["3"],
                 header_row=None))

# Set  split4  name to  4
w.add(dw.SetName(column=["split4"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["4"],
                 header_row=None))

# Fold   using  header as a key
w.add(dw.Fold(column=[],
              table=0,
              status="active",
              drop=False,
              keys=[-1]))

# Extract from value between '|' and '}'
w.add(dw.Extract(column=["value"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before="}",
                 after="\\|",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Fill extract  with values from above
w.add(dw.Fill(column=["extract"],
              table=0,
              status="active",
              drop=False,
              direction="down",
              method="copy",
              row=None))

# Split value repeatedly on ','  into  rows
w.add(dw.Split(column=["value"],
               table=0,
               status="active",
               drop=True,
               result="row",
               update=False,
               insert_position="right",
               row=None,
               on=",",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max="0",
               positions=None,
               quote_character=None))

# Extract from value on '[0-9]{4}'
w.add(dw.Extract(column=["value"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on="[0-9]{4}",
                 before=None,
                 after=None,
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Delete  rows where fold = 'split'
w.add(dw.Filter(column=[],
                table=0,
                status="active",
                drop=False,
                row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="fold",
            value="split",
            op_str="=")])))

# Delete  rows where value starts with 'center'
w.add(dw.Filter(column=[],
                table=0,
                status="active",
                drop=False,
                row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.StartsWith(column=[],
                    table=0,
                    status="active",
                    drop=False,
                    lcol="value",
                    value="center",
                    op_str="starts with")])))

# Drop value
w.add(dw.Drop(column=["value"],
              table=0,
              status="active",
              drop=True))

# Set  fold  name to  Rank
w.add(dw.SetName(column=["fold"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Rank"],
                 header_row=None))

# Set  extract1  name to  Year
w.add(dw.SetName(column=["extract1"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Year"],
                 header_row=None))

# Set  extract  name to  Country
w.add(dw.SetName(column=["extract"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Country"],
                 header_row=None))

w.apply_to_file(sys.argv[1]).print_csv(sys.argv[2])

