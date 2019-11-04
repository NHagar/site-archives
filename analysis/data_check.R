library(tidyverse)
library(lubridate)

df <- read_csv("../pacific-standard/ps-archive.csv")


df %>% filter((pub_date>=date("2016-04-01")) & (pub_date<=date("2017-02-28"))) %>% select(link, hed, sections, byline, pub_date, tags) %>% write_csv('ps_check.csv')
