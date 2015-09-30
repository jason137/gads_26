=== data warmup ===

    head toy.data
    tail toy.data
    wc toy.data
    wc -l toy.data
    man wc
    
    less toy.data --> scrolling, pattern matching
    grep test1 toy.data
    grep test1$ toy.data --> regexes!
    
    cat toy.data | grep test1
    cat toy.data | grep test1$
    cat toy.data | grep test1\\$ --> escape chars!
   
    head toy.data | sed 's/test/waffle/'
    head toy.data | sed 's/t//'
    head toy.data | sed 's/t//g'

=== citibike dataset ===

goal: let's clean this dataset up
    
what does the data look like?

    head citibike.csv
    wc -l citibike.csv
    less citibike.csv
    /False
    
which stations are test stations?

    less citibike.csv
    /True
    cat citibike.csv | grep True
    --> no test stations, so this field is useless
    
it looks like name & addr1 are the same...how can we verify this?

=== awk ===

    # print the whole line
    head citibike.csv | awk -F, '{print}'
    head citibike.csv | awk -F, '{print $0}'

    # perform simple field extractions 
    # (can be done more simply with cut...man cut to check it out)
    head citibike.csv | awk -F, '{print $1}'
    head citibike.csv | awk -F, '{print $2}'
    head citibike.csv | awk -F, '{print $3}'
    head citibike.csv | awk -F, '{print $1, $2, $3}'

    # specify output delim (output field separator)
    head citibike.csv | awk -F, 'BEGIN {OFS=","} {print $1, $2, $3}'

    # here's where awk starts killing it
    head citibike.csv | awk -F, '{if ($2==$3) print}'
    head citibike.csv | awk -F, '{if ($2!=$3) print}'
    cat citibike.csv | awk -F, '{if ($2!=$3) print $0}'

    # some flashy shorthand
    head citibike.csv | awk -F, '($2==$3) {print}'
    head citibike.csv | awk -F, '($2!=$3) {print}'

fields 2 & 3 are the same (modulo some unimportant differences), so we only
need one of these

does each record have the same number of fields?

    # print num fields
    head citibike.csv | awk -F, '{print NF}'

    # print last field
    head citibike.csv | awk -F, '{print $NF}'

    # display unique field counts
    cat citibike.csv | awk -F, '{print $NF}' | sort | uniq

    # display frequency distribution of field counts
    cat citibike.csv | awk -F, '{print $NF}' | sort | uniq -c

this agrees with output of `wc -l`, so all recs have the same number of fields
    
does any record have an addr2?

    cat citibike.csv | awk -F, '{if ($4!="") print $4}'

the addr2 fields that do exist don't look useful...we don't need this field either
    
how can we look at the last 3 fields?

    head citibike.csv | awk -F, 'BEGIN {OFS=","} {print $10, $11, $12}'
    head citibike.csv | awk -F, 'BEGIN {OFS=","} {print $(NF-2), $(NF-1), $NF}'

    cat citibike.csv | awk -F, 'BEGIN {OFS=","} {print $10, $11, $12}'
    cat citibike.csv | awk -F, 'BEGIN {OFS=","} {print $10, $11, $12}' | sort | uniq -c
   
which stations are not in service?

    cat citibike.csv | grep "Not In Service" 
    grep "Not In Service" citibike.csv

what about the status_key?

    cat citibike.csv | awk -F, 'BEGIN {OFS=","} {if ($11==3) print}'

so these fields encode the same info...we only need one

the fields we want to keep are:

    id, name, addr1, lat, lon, bikes_avail, spots_avail, spots_total, status_val

let's create a new file using awk

    head -n1 citibike.csv | awk -F, 'BEGIN {OFS=","} {print $1, $2, $3, $5, $6, $7, $8, $9, $10}'
    cat citibike.csv | awk -F, 'BEGIN {OFS=","} {print $1, $2, $3, $5, $6, $7, $8, $9, $10}' > new_citibike.csv

here's a more compact version using gcut (installed via homebrew)

    head -n1 citibike.csv | gcut -d, -f4,11,12 --complement
    cat citibike.csv | gcut -d, -f2,4,11,12 --complement > new_citibike.csv

notice cut & gcut are different! (osx vs gnu)

=== addl questions ===
- which station has the most total spots?
- which station has the highest pct of bikes available (at the time this file
  was created)?
- suppose you wanted to create a visualization to represent this dataset. what
  fields would you want to use? why? how would you use them?
- suppose you have an incoming stream of messages containing lat/lon info. how
  could you determine which station is the closest for each message?
- create a python script that parses the original citibike.json into a file
  like citibike.csv

