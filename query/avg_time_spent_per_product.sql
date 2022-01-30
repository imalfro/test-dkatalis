select 
    product,
    sub_product,
    sum(to_timestamp(ser_time,'HH24:MI:SS')::TIME) total_time_spent,
    count(1) no_of_complaints,
    sum(to_timestamp(ser_time,'HH24:MI:SS')::TIME) avg_time_spent_per_complain
from dkatalis_crm.crm_events a
inner join dkatalis_crm.crm_call_center_logs b 
on a.complaint_id = b.complaint_id 
group by product, sub_product;