from testscripts.api.coccoc_new_feeds_v2.common import NewFeedCommon;
from databases.sql.coccoc_new_feeds_db import NewFeedDB;

class TestNewFeedCralwer:
    common = NewFeedCommon()
    newfeed_db = NewFeedDB()
    result = True
    expect_file = "expect.txt"
    actual_file = "actual.txt"
    diff_file = "diff.txt"
    common_file = "common.txt"

    # SKip check cityhash64 because cannot install

    # BRBE-779: Get all discover urls in links
    def test_get_discover_urls(self):
        # Get by expectation script
        list_datafeeds = []
        list_domain = self.get_list_sources_db()
        for domain in list_domain:
            self.set_filename(domain)
            list_sublinks = []
            # Get url from link
            list_datafeed_url = self.get_list_datafeeds_db(domain, type="link")
            list_datafeeds += list_datafeed_url
            for url in list_datafeed_url:
                print(domain, ": ", url)
                url = url.lstrip() # Trip enter character
                sublinks = self.common.get_sub_links_are_article(url)
                sublinks = self.common.remove_not_sub_links_in_list(domain, sublinks)
                sublinks = self.common.remove_invalid_links_in_list(sublinks, ['#box_comment_vne'])
                sublinks = self.common.replace_string_in_list(sublinks, '//', '/')
                sublinks = self.common.replace_string_in_list(sublinks, ':/', '://')

                list_sublinks += sublinks

            # Get url from rss
            list_datafeed_rss = self.get_list_datafeeds_db(domain, type = "rss")
            list_datafeeds += list_datafeed_rss
            for rss in list_datafeed_rss:
                rss = rss.lstrip()  # Trip enter character
                sublinks = self.common.get_sub_links_in_rss_feed(rss)
                list_sublinks += sublinks

            list_sublinks = self.common.remove_duplicated_items_in_list(list_sublinks)
            self.common.write_to_file(self.expect_file, list_sublinks)
            self.common.write_to_file("Data/1_datafeeds.txt", list_datafeeds)

            # Get in DB
            list_article_url = self.get_article_url_db(domain)
            self.common.write_to_file(self.actual_file, list_article_url)

    # Make sure all domains have discover links
    def test_verfiy_domain_has_discover_link(self):
        list_domain = self.get_list_sources_db()
        list_domain_error = []
        list_datafeed_error = []
        for domain in list_domain:
            list_datafeed = self.get_list_datafeeds_db(domain)
            if not len(list_datafeed):
                datafeed_error = self.get_list_datafeeds_db(domain, type="link", status=None)
                list_domain_error.append(domain)
                list_datafeed_error.append(datafeed_error)
                self.result = False
        if len(list_domain_error):
            print("ERROR: domains have no discover active url ")
            for i in range(len(list_domain_error)):
                print("    ", list_domain_error[i], ": ", list_datafeed_error[i])
        print("ERROR: domains have no discover active url ")
        self.common.print_list(list_domain_error)
        assert self.result == True

    # Make sure all domains have discover rss
    def test_verfiy_domain_has_discover_rss(self):
        list_domain = self.get_list_sources_db()
        list_domain_error = []
        list_datafeed_error = []
        for domain in list_domain:
            list_datafeed = self.get_list_datafeeds_db(domain, type = "rss")
            if not len(list_datafeed):
                datafeed_error = self.get_list_datafeeds_db(domain, type="rss", status=None)
                list_domain_error.append(domain)
                list_datafeed_error.append(datafeed_error)
                self.result = False
        if len(list_domain_error):
            print("ERROR: domains have no discover active rss ")
            for i in range(len(list_domain_error)):
                print("    ", list_domain_error[i], ": ", list_datafeed_error[i])
        print("ERROR: domains have no discover active rss ")
        self.common.print_list(list_domain_error)
        assert self.result == True

    # Make sure all dicovers url are live
    def test_verify_discover_url_are_live(self):
        list_active_link = self.get_active_link_db()
        for link in list_active_link:
            result = self.common.check_link_is_alive(link)
            if result == False:
                print(link)
                self.result = False
        assert self.result == True

    # Make sure all urls / rss in source_datafeeds belong to correct domains
    def test_verify_discover_url_belong_correct_domain(self):
        list_domain = self.get_list_sources_db()
        list_domain_rss_error = []
        list_domain_link_error = []
        list_datafeed_rss_error = []
        list_datafeed_link_error = []
        for domain in list_domain:
            list_datafeed_rss = self.get_list_datafeeds_db(domain, type="rss", status = None)
            list_datafeed_link = self.get_list_datafeeds_db(domain, type="link", status = None)
            datafeed_rss_error = self.common.get_items_in_list_not_contains(list_datafeed_rss, domain)
            datafeed_link_error = self.common.get_items_in_list_not_contains(list_datafeed_link, domain)
            if len(datafeed_rss_error):
                list_domain_rss_error.append(domain)
                list_datafeed_rss_error.append(datafeed_rss_error)
                self.result = False
            if len(datafeed_link_error):
                list_domain_link_error.append(domain)
                list_datafeed_link_error.append(datafeed_link_error)
                self.result = False

        for i in range(len(list_domain_rss_error)):
            print("ERROR: Invalid rss: ", list_domain_rss_error[i], list_datafeed_rss_error[i])
        for i in range(len(list_domain_link_error)):
            print("ERROR: Invalid url: ", list_domain_link_error[i], list_datafeed_link_error[i])
        assert self.result == True

    # BRBE-779: Check no duplicated url
    def test_verify_duplicated_article_url(self):
        # Get by expectation script
        list_domain = self.get_list_sources_db()
        # Compare values between expect and actual
        for domain in list_domain:
            self.set_filename(domain)
            list_duplicated = self.common.get_duplicated_items_in_file(self.actual_file);
            if len(list_duplicated):
                print(domain, ": Duplicated url:")
                self.common.print_list(list_duplicated)
                self.result = False
        assert self.result == True

    # BRBE-779: Check all article urls belong correct domains
    def test_verify_article_url_belong_correct_domain(self):
        # Get by expectation script
        list_domain = self.get_list_sources_db()
        # Compare values between expect and actual
        for domain in list_domain:
            self.set_filename(domain)
            article_url_error = self.common.get_items_in_file_not_contains(self.actual_file, domain)
            if len(article_url_error):
                print("ERROR: ", domain, " contains incorrect article url")
                self.common.print_list(article_url_error)
                self.result = False
        assert self.result == True

    # BRBE-779: Check all article urls are live
    def test_verify_article_url_are_live(self):
        # Get by expectation script
        list_domain = self.get_list_sources_db()
        # Compare values between expect and actual
        for domain in list_domain:
            self.set_filename(domain)
            article_url_error = self.common.get_all_links_in_file_are_not_alive(self.actual_file)
            if len(article_url_error):
                print("ERROR: ", domain, " contains incorrect article url")
                self.common.print_list(article_url_error)
                self.result = False
        assert self.result == True

    # BRBE-779: Check discover link in core - verify values between expect and actual data
    def test_verify_coverage_discover_url_by_link(self):
        # Get by expectation script
        list_domain = self.get_list_sources_db()
        # Compare values between expect and actual
        for domain in list_domain:
            self.set_filename(domain)
            self.calculate_ratio_of_common_links(domain);

    # BRBE-779: Verify city hash 64
    def test_verify_cityhash64(self):
        # Get by expectation script
        list_domain = self.get_list_sources_db()
        # Compare values between expect and actual
        for domain in list_domain:
            list_url = self.get_article_url_db(domain)
            for url in list_url:
                cityhash = self.common.get_cityhash64(url)
                print(cityhash)

    def calculate_ratio_of_common_links(self, domain):
        self.common.get_different_elements_between_files(self.expect_file, self.actual_file, self.diff_file)
        self.common.get_common_value_between_files(self.expect_file, self.actual_file, self.common_file)

        number_common = self.common.get_number_of_lines(self.common_file)
        number_diff = self.common.get_number_of_lines(self.diff_file)
        number_expect = self.common.get_number_of_lines(self.expect_file)
        number_actual = self.common.get_number_of_lines(self.actual_file)

        if number_expect > number_actual or number_actual == 0:
            print(domain, ": NOTICE!! PLEASE CHECK!!!!")
        else:
            print(domain)
        print("    Number of expect article url: %d" % (number_expect))
        print("    Number of actual article url: %d" % (number_actual))
        ratio = self.common.division_percentage(number_common, number_actual);
        print("    Common ratio on actual: %d %%" % (ratio))
        ratio = self.common.division_percentage(number_common, number_expect);
        print("    Common ratio on expect: %d %%" % (ratio))
        ratio = self.common.division_percentage(number_diff, number_actual);
        print("    Diff ratio on actual  : %d %%" % (ratio))
        ratio = self.common.division_percentage(number_diff, number_expect);
        print("    Diff ratio on expect  : %d %%" % (ratio))


    def get_list_sources_db(self):
        db_source = self.newfeed_db.get_newfeeds_db(f'select distinct(domain) from coccoc_news_feed.source_datafeeds;')
        list_source = self.newfeed_db.get_list_db(db_source)
        return list_source

    # Type = link | rss by domain
    def get_list_datafeeds_db(self, domain, type = 'link', status = 'active'):
        if status == 'active':
            query = f'SELECT url FROM coccoc_news_feed.source_datafeeds where domain = "{domain}" and status = "{status}" and type = "{type}";'
        else:
            query = f'SELECT url FROM coccoc_news_feed.source_datafeeds where domain = "{domain}" and status != "{status}" and type = "{type}";'
        db_datafeed = self.newfeed_db.get_newfeeds_db(query)
        list_datafeed = self.newfeed_db.get_list_db(db_datafeed)
        return list_datafeed

    # Get all article_url by domain in DB
    def get_article_url_db(self, domain):
        db_article_url = self.newfeed_db.get_newfeeds_db(f'SELECT url FROM coccoc_news_feed.article_urls where domain = "{domain}";')
        list_article_url = self.newfeed_db.get_list_db(db_article_url)
        return list_article_url

    # Get all active url
    def get_active_link_db(self):
        db_active_link = self.newfeed_db.get_newfeeds_db(
            f'SELECT url FROM coccoc_news_feed.source_datafeeds where type = "link" and status = "active";')
        list_active_link = self.newfeed_db.get_list_db(db_active_link)
        return list_active_link

    # Get filename
    def get_expected_filename(self, domain):
        return "Data/" + domain + "_expected.txt"

    # Get filename
    def get_actual_filename(self, domain):
        return "Data/" + domain + "_actual.txt"

    # Set filename
    def set_filename(self, domain):
        self.expect_file = "Data/" + domain + "_expected.txt"
        self.actual_file = "Data/" + domain + "_actual.txt"
        self.diff_file = "Data/" + domain + "_diff.txt"
        self.common_file = "Data/" + domain + "_comm.txt"