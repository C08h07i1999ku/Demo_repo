from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class Test_HRMS:
    def hrms(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://wscdemo.eduleadonline.com/")
        login_email_field = driver.find_element(By.XPATH,"//input[@id='login_email']")
        login_email_field.send_keys("Administrator")
        password_field = driver.find_element(By.XPATH,"//input[@id='login_password']")
        password_field.send_keys("admin@123")
        time.sleep(3)
        login_button = driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
        login_button.click()
        time.sleep(10)
        hrms_button = driver.find_element(By.XPATH,"//a[@title='HRMS (Base)']")
        hrms_button.click()
        time.sleep(5)
        # employment_type_button = driver.find_element(By.XPATH,"//span[normalize-space()='Employment Type']")
        # employment_type_button.click()
        # time.sleep(3)
        # add_employment_type = driver.find_element(By.XPATH,"//span[@data-label='Add%20Employment%20Type']")
        # add_employment_type.click()
        # time.sleep(2)
        # employment_type_field = driver.find_element(By.XPATH,"//input[@class='input-with-feedback form-control bold']")
        # employment_type_field.send_keys("project wise")
        # time.sleep(2)
        # save_button = driver.find_element(By.XPATH,"//div[@class='modal fade show']//button[@type='button'][normalize-space()='Save']")
        # save_button.click()
        # time.sleep(3)
        # driver.back()
        # campus_location_button = driver.find_element(By.XPATH,"//span[normalize-space()='Campus Location']")
        # campus_location_button.click()
        # time.sleep(3)
        # add_campus_location_button = driver.find_element(By.XPATH,"//span[@data-label='Add%20Campus%20Location']")
        # add_campus_location_button.click()
        # campus_location_field = driver.find_element(By.XPATH,"//div[@data-fieldname='branch']//input[@type='text']")
        # campus_location_field.send_keys("Remuna")
        # time.sleep(3)
        # save_button = driver.find_element(By.XPATH,"//div[@class='modal fade show']//button[@type='button'][normalize-space()='Save']")
        # save_button.click()
        # department_button = driver.find_element(By.XPATH,"//span[normalize-space()='Department']")
        # department_button.click()
        # time.sleep(5)
        # add_department_button = driver.find_element(By.XPATH,"//span[@data-label='Add%20Department']")
        # add_department_button.click()
        # time.sleep(5)
        # department_field = driver.find_element(By.XPATH,"//div[@data-fieldname='department_name']//input[@type='text']")
        # department_field.send_keys("social media")
        # department_alias_field = driver.find_element(By.XPATH,"//div[@data-fieldname='department_alias']//input[@type='text']")
        # department_alias_field.send_keys("videography")
        # parent_department_field = driver.find_element(By.XPATH,"//div[@data-fieldname='parent_department']//input[@role='combobox']")
        # parent_department_field.send_keys("school of services")
        # time.sleep(5)
        # school_of_services = driver.find_element(By.XPATH,"//strong[normalize-space()='School Of Services - WSC']")
        # school_of_services.click()
        # time.sleep(5)
        # payroll_cost_centre = driver.find_element(By.XPATH,"//div[@data-fieldname='payroll_cost_center']//input[@role='combobox']")
        # payroll_cost_centre.send_keys("main")
        # time.sleep(5)
        # main_wsc = driver.find_element(By.XPATH,"//strong[normalize-space()='Main - WSC']")
        # main_wsc.click()
        # time.sleep(5)
        # add_row = driver.find_element(By.XPATH,"//div[@data-fieldname='shift_request_approver']//button[@class='btn btn-xs btn-secondary grid-add-row'][normalize-space()='Add Row']")
        # add_row.click()
        # time.sleep(5)
        # approver_field = driver.find_element(By.XPATH,"//div[@class='col grid-static-col col-xs-10 error bold']")
        # approver_field.click()
        # time.sleep(5)
        # nitesh_kumar = driver.find_element(By.XPATH,"//strong[normalize-space()='1niteshkumarojha@gmail.com']")
        # nitesh_kumar.click()
        # time.sleep(5)
        # add_row2 = driver.find_element(By.XPATH,"//div[@data-fieldname='leave_approvers']//button[@class='btn btn-xs btn-secondary grid-add-row'][normalize-space()='Add Row']")
        # add_row2.click()
        # time.sleep(5)
        # leave_approver = driver.find_element(By.XPATH,"//div[@class='data-row row']//div[@class='col grid-static-col col-xs-10 error bold']")
        # leave_approver.click()
        # time.sleep(5)
        # amitpritam = driver.find_element(By.XPATH,"//div[@class='data-row row editable-row']//strong[contains(text(),'1234amitpritam@gmail.com')]")
        # amitpritam.click()
        # time.sleep(5)
        # add_row3 = driver.find_element(By.XPATH,"//div[@data-fieldname='expense_approvers']//button[@class='btn btn-xs btn-secondary grid-add-row'][normalize-space()='Add Row']")
        # add_row3.click()
        # time.sleep(5)
        # expense_approver = driver.find_element(By.XPATH,"//div[@data-fieldname='expense_approvers']//div[@class='col grid-static-col col-xs-10 error bold']")
        # expense_approver.click()
        # time.sleep(5)
        # siba_behera = driver.find_element(By.XPATH,"//div[@class='data-row row editable-row']//strong[contains(text(),'143srikrushna@gmail.com')]")
        # siba_behera.click()
        # time.sleep(5)
        # save_button = driver.find_element(By.XPATH,"//button[@data-label='Save']")
        # # Scroll and click the button through JavaScript
        # driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", save_button)
        # time.sleep(5)

        # designation_button = driver.find_element(By.XPATH,"//span[@class='link-content ellipsis'][normalize-space()='Designation']")
        # designation_button.click()
        # time.sleep(5)
        # add_designation_button = driver.find_element(By.XPATH,"//span[@data-label='Add%20Designation']")
        # add_designation_button.click()
        # time.sleep(3)
        # designation = driver.find_element(By.XPATH,"//body/div[@class='modal fade show']/div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body ui-front']/div/div[@class='form-layout']/div[@class='form-page']/div[@class='row form-section visible-section']/div[@class='section-body']/div[@class='form-column col-sm-12']/form/div[@class='frappe-control input-max-width']/div[@class='form-group']/div[@class='control-input-wrapper']/div[@class='control-input']/input[1]")
        # designation.send_keys("cameraman")
        # appraisal_template = driver.find_element(By.XPATH,"//div[@class='modal fade show']//div[@class='modal-dialog']//div[@class='modal-content']//div[@class='modal-body ui-front']//div//input[@role='combobox']")
        # appraisal_template.click()
        # time.sleep(5)
        # appraisal_template_10 = driver.find_element(By.XPATH,"//div[@class='modal fade show']//div[@class='modal-dialog']//div[@class='modal-content']//div[@class='modal-body ui-front']//div//strong[contains(text(),'Appraisal template 10')]")
        # appraisal_template_10.click()
        # time.sleep(5)
        # save_button = driver.find_element(By.XPATH,"//div[@class='modal fade show']//button[@type='button'][normalize-space()='Save']")
        # save_button.click()
        # time.sleep(5)

        # employee_grade = driver.find_element(By.XPATH,"//span[normalize-space()='Employee Grade']")
        # employee_grade.click()
        # time.sleep(3)
        # add_employee_grade_button = driver.find_element(By.XPATH,"//span[@data-label='Add%20Employee%20Grade']")
        # add_employee_grade_button.click()
        # time.sleep(3)
        # name = driver.find_element(By.XPATH,"//div[@data-fieldname='__newname']//input[@type='text']")
        # name.send_keys("outrageous")
        # salary_structure = driver.find_element(By.XPATH,"//div[@data-fieldname='default_salary_structure']//input[@role='combobox']")
        # salary_structure.click()
        # time.sleep(3)
        # employment_2024 = driver.find_element(By.XPATH,"//strong[normalize-space()='Employment (2024-25)']")
        # employment_2024.click()
        # time.sleep(5)
        # save_button = driver.find_element(By.XPATH,"//div[@id='page-Employee Grade']//button[@data-label='Save']")
        # save_button.click()
        # time.sleep(5)
        # driver.quit()
        #
        # employee_group = driver.find_element(By.XPATH,"//span[normalize-space()='Employee Group']")
        # employee_group.click()
        # time.sleep(3)
        # add_employee_group = driver.find_element(By.XPATH,"//span[@data-label='Add%20Employee%20Group']")
        # add_employee_group.click()
        # time.sleep(3)
        # employee_group_name_field = driver.find_element(By.XPATH,"//div[@data-fieldname='employee_group_name']//input[@type='text']")
        # employee_group_name_field.send_keys("Videographers")
        # time.sleep(3)
        # save_button = driver.find_element(By.XPATH,"//div[@class='modal fade show']//button[@type='button'][normalize-space()='Save']")
        # save_button.click()

        # holiday_list_button = driver.find_element(By.XPATH,"//span[normalize-space()='Holiday List']")
        # holiday_list_button.click()
        # time.sleep(3)
        # add_holiday_list_button = driver.find_element(By.XPATH,"//span[@data-label='Add%20Holiday%20List']")
        # add_holiday_list_button.click()
        # time.sleep(5)
        # holiday_list_name = driver.find_element(By.XPATH,"//div[@data-fieldname='holiday_list_name']//input[@type='text']")
        # holiday_list_name.send_keys("mahashivratri")
        # time.sleep(3)
        # from_date = driver.find_element(By.XPATH,"//input[@data-fieldname='from_date']")
        # from_date.click()
        # time.sleep(3)
        # starting_date = driver.find_element(By.XPATH,"//body/div[@id='datepickers-container']/div[1]/div[1]/div[1]/div[2]/div[3]")
        # starting_date.click()
        # time.sleep(5)
        # to_date = driver.find_element(By.XPATH,"//input[@data-fieldname='to_date']")
        # to_date.click()
        # time.sleep(5)
        # ending_date = driver.find_element(By.XPATH,"//body/div[@id='datepickers-container']/div[2]/div[1]/div[1]/div[2]/div[30]")
        # ending_date.click()
        # time.sleep(5)
        # add_row_button = driver.find_element(By.XPATH,"//button[normalize-space()='Add Row']")
        # add_row_button.click()
        # time.sleep(5)
        # date_field = driver.find_element(By.XPATH,"//div[@class='col grid-static-col col-xs-5 error bold']")
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable(date_field))
        # date_field.click()
        # time.sleep(5)
        # date = driver.find_element(By.XPATH,"//body/div[@id='datepickers-container']/div[3]/div[1]/div[1]/div[2]/div[3]")
        # date.click()
        # time.sleep(5)
        # description_box = driver.find_element(By.XPATH,"//textarea[@placeholder='Description']")
        # description_box.click()
        # time.sleep(5)
        # description_box.send_keys("It is a holiday")
        # time.sleep(5)
        # save_button = driver.find_element(By.XPATH,"//button[@data-label='Save']")
        # save_button.click()
        # time.sleep(5)

        job_requisition = driver.find_element(By.XPATH,"//a[@title='Job Requisition']")
        job_requisition.click()
        time.sleep(3)
        add_job_requisition = driver.find_element(By.XPATH,"//span[@data-label='Add%20Job%20Requisition']")
        add_job_requisition.click()
        time.sleep(3)
        designation_field = driver.find_element(By.XPATH,"//div[@data-fieldname='designation']//div[@class='form-group']//input[@role='combobox']")
        designation_field.click()
        time.sleep(5)
        designation_field.send_keys("cameraman")
        time.sleep(3)
        cameraman = driver.find_element(By.XPATH,"//strong[normalize-space()='cameraman']")
        cameraman.click()
        time.sleep(3)
        department = driver.find_element(By.XPATH,"//div[@data-fieldname='department']//input[@role='combobox']")
        department.click()
        time.sleep(5)
        department.send_keys("social media")
        time.sleep(3)
        social_media = driver.find_element(By.XPATH,"//strong[normalize-space()='social media - WSC']")
        social_media.click()
        time.sleep(3)
        employment_type = driver.find_element(By.XPATH,"//div[@data-fieldname='employment_type']//input[@role='combobox']")
        employment_type.click()
        time.sleep(3)
        employment_type.send_keys("project wise")
        time.sleep(5)
        employment_type.send_keys(Keys.TAB)
        no_of_positions = driver.find_element(By.XPATH,"//input[@data-fieldtype='Int']")
        no_of_positions.click()
        time.sleep(3)
        no_of_positions.send_keys(5)
        expected_compensations = driver.find_element(By.XPATH,"//input[@data-fieldtype='Currency']")
        expected_compensations.click()
        time.sleep(3)
        expected_compensations.clear()
        expected_compensations.send_keys(20000)
        time.sleep(3)
        expected_compensations.send_keys(Keys.TAB)
        time.sleep(3)
        company = driver.find_element(By.XPATH,"//div[@data-fieldname='company']//input[@role='combobox']")
        company.click()
        company.send_keys(Keys.TAB)
        time.sleep(3)
        status = driver.find_element(By.XPATH,"//select[@class='input-with-feedback form-control ellipsis bold']")
        status.send_keys(Keys.TAB)
        time.sleep(3)
        requested_by = driver.find_element(By.XPATH,"//div[@data-fieldname='requested_by']//div[@class='form-group']//input[@role='combobox']")
        requested_by.send_keys("vikram sharma")
        requested_by.send_keys(Keys.ENTER)
        time.sleep(3)
        requested_by.send_keys(Keys.TAB)
        posting_date = driver.find_element(By.XPATH,"//input[@data-fieldname='posting_date']")
        posting_date.send_keys(Keys.TAB)
        expected_date = driver.find_element(By.XPATH,"//input[@data-fieldname='expected_by']")
        time.sleep(5)
        my_date = driver.find_element(By.XPATH,"//body/div[@id='datepickers-container']/div[2]/div[1]/div[1]/div[2]/div[30]")
        my_date.click()
        time.sleep(3)
        job_description = driver.find_element(By.XPATH,"//a[@id='job-requisition-job_description_tab-tab']")
        job_description.click()
        time.sleep(5)
        description_field = driver.find_element(By.XPATH,"//div[@class='ql-container ql-snow']//div[@class='ql-editor ql-blank']")
        description_field.send_keys("We are looking for a videographer,who must have the experience of hands on experience in recording good quality videos and also this is a onsite job.")
        time.sleep(5)
        save_button = driver.find_element(By.XPATH,"//button[@data-label='Save']")
        save_button.click()
        time.sleep(3)
        actions_button = driver.find_element(By.XPATH,"//div[@class='actions-btn-group']//button[@type='button']")
        actions_button.click()
        time.sleep(3)
        save = driver.find_element(By.XPATH,"//ul[@class='dropdown-menu dropdown-menu-right show']//span[@data-label='Save']")
        save.click()

module = Test_HRMS()
module.hrms()
