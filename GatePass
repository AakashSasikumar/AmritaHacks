import com.ui4j.api.browser.BrowserEngine;
import com.ui4j.api.browser.BrowserFactory;
import com.ui4j.api.browser.Page;
import com.ui4j.api.dom.Document;

import java.util.concurrent.TimeUnit;

/**
 * Created by Aakash on 2/22/2017.
 */
public class Main {
    public static void main(String[] args) throws InterruptedException {
        BrowserEngine browser = BrowserFactory.getWebKit();
        Page page = browser.navigate("http://cms.amritanet.edu/login");//login page
        Document document = page.getDocument();
        document.query("input[type='text']").get().setValue("CB.EN.U4CSE15301");//username
        document.query("input[type='password']").get().setValue("***********");//password
        document.query("button[type='submit']").get().click();
        TimeUnit.SECONDS.sleep(5);
        document.query("a[href='http://cms.amritanet.edu/gate-passes/apply']").get().click();//applying gate pass
        //document.query("a[href='http://cms.amritanet.edu/gate-passes/apply']").get().click();

        document.query("option[value ='day_pass']").get().click();
        page.executeScript("var element = document.getElementById('pass_type'); element.value = \"day_pass\";");//setting the type of pass
        document.query("input[id='from_date']").get().setValue("22/02/2017");//setting the date

        page.show();
    }
}
