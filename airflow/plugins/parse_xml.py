from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import sys
import pandas as pd
import re
 
from utils.Model_PDFClass import MetaDataPDF, ContentPDF

xml_path = os.getenv('AIRFLOW_FILES_PATH')

FILES= {'content':[],'metadata':[]}
METADATA_FILES = []
CONTENT_FILES = []

def find_xml_files(folder_path):
    # Initialize an empty list to store matching filenames
    global FILES, METADATA_FILES, CONTENT_FILES
    
    # Walk through the specified folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        # Iterate over the list of files to check if they end with "_content.xml"
        for file in files:
            if file.endswith("_content.xml"):
                # If so, add the file's full path to the list
                FILES['content'].append(os.path.join(root, file))

            if file.endswith("_metadata.xml"):
                # If so, add the file's full path to the list
                FILES['metadata'].append(os.path.join(root, file))
    METADATA_FILES = FILES['metadata']
    CONTENT_FILES = FILES['content']
    METADATA_FILES.sort()
    CONTENT_FILES.sort()



class Dataset:
 
    def __init__(self, user_id):
        self.metadata = []
        self.content = []
        self.load_data(user_id)
 
    def load_data(self,user_id):
        self.parse_metadata()
        self.parse_content(user_id)
 
    def parse_metadata(self):
    # Define a dictionary to map doc_id to preset titles
        preset_titles = {1: "2024 Level I Topic Outlines", 2: "2024 Level II Topic Outlines", 3: "2024 Level III Topic Outlines"}
 
        for i, file in enumerate(METADATA_FILES):
            soup = BeautifulSoup(open(file), 'xml')
 
            file_path_name = soup.find('Filename').text # type: ignore
            filename = os.path.basename(file_path_name)
            idno = soup.find('Idno').text # type: ignore
 
            # Use calculate_year and calculate_level methods here
            year = self.calculate_year(filename)
            level = self.calculate_level(filename)
 
            # Use the preset title if available, otherwise use the default title from the XML
            title = preset_titles.get(i + 1, soup.find('Title').text) # type: ignore
 
            print(filename)
            print(title)
            print(idno)
            print(year)
            print(level)

            metadata = MetaDataPDF(
                doc_id=i + 1,
                filename=filename,
                title=title,
                idno=idno,
                year=year,
                level=level,
            )
 
            self.metadata.append(metadata)
 
    def parse_content(self,user_id):
        for metadata, content_file in zip(self.metadata, CONTENT_FILES):
            soup = BeautifulSoup(open(content_file), 'xml')
 
            doc_id = metadata.doc_id
 
            current_topic = None
            current_section_title = None
            contents = []
 
            # Added flag to check if we are in the initial section before the first 'topic' <head>
            in_initial_section = True
 
            for div in soup.find_all('div'):
                head = div.find('head')
                if head and 'LEARNING OUTCOMES' in head.text:
                    # We have found a topic
                    current_topic = head.find_previous('head').text.strip() if head.find_previous('head') else None
                    # Turn off the flag once we reach the first 'topic' <head>
                    in_initial_section = False
                elif head and in_initial_section:
                    # We are in the initial section, process <head> as section_title
                    current_section_title = head.text.strip()
 
                    # Check if the next <head> is not 'LEARNING OUTCOMES' before processing as a new section_title
                    next_head = head.find_next('head')
                    if next_head and 'LEARNING OUTCOMES' not in next_head.text:
                        paragraph_text = '\n'.join([s.text.strip() for s in div.find_all(['s', 'p'])])
                        if paragraph_text or not div.find(['s', 'p']):
                            paragraph_text = paragraph_text.replace('\n', ' ').strip()
 
                            # Process paragraph_text using the existing method
                            paragraph_text = self.process_paragraph_text(paragraph_text)
 
                            # Map the level while creating ContentPDF instance
                            level_mapping = {'l1': 'Level I', 'l2': 'Level II', 'l3': 'Level III'}
                            level = level_mapping.get(metadata.level, metadata.level)
 
                            # Set default blank topic based on level
                            if not current_topic and level == 'Level I':
                                current_topic = 'Quantitative Methods'
                            elif not current_topic and level == 'Level II':
                                current_topic = 'Quantitative Methods'
                            elif not current_topic and level == 'Level III':
                                current_topic = 'Economics'
 
                            content = ContentPDF(
                                user_id = user_id,
                                content_id=len(contents) + 1,
                                doc_id=doc_id,
                                level=level,
                                year=metadata.year,
                                topic=current_topic,
                                section_title=current_section_title,
                                paragraph_text=paragraph_text,
                            )
                            contents.append(content)
 
                elif head and current_topic is not None:
                    # We are inside the section with <p><s> tags
                    next_head = head.find_next('head')
                    if next_head and 'LEARNING OUTCOMES' in next_head.text:
                        # Skip the current head as section_title if the next head has 'LEARNING OUTCOMES'
                        current_section_title = None
                    else:
                        current_section_title = head.text.strip()
 
                        paragraph_text = '\n'.join([s.text.strip() for s in div.find_all(['s', 'p'])])
                        if paragraph_text or not div.find(['s', 'p']):
                            paragraph_text = paragraph_text.replace('\n', ' ').strip()
 
                            # Process paragraph_text using the existing method
                            paragraph_text = self.process_paragraph_text(paragraph_text)
 
                            # Map the level while creating ContentPDF instance
                            level_mapping = {'l1': 'Level I', 'l2': 'Level II', 'l3': 'Level III'}
                            level = level_mapping.get(metadata.level, metadata.level)
 
                            content = ContentPDF(
                                user_id = user_id,
                                content_id=len(contents) + 1,
                                doc_id=doc_id,
                                level=level,
                                year=metadata.year,
                                topic=current_topic,
                                section_title=current_section_title,
                                paragraph_text=paragraph_text,
                            )
                            contents.append(content)
 
            self.content.extend(contents)
 
    def calculate_level(self, filename):
        # Implement logic to calculate level based on filename
        return filename.split('-')[1].lower()
 
    def calculate_year(self, filename):
        # Implement logic to calculate year based on filename
        return int(filename.split('-')[0])
 
    def process_paragraph_text(self, paragraph_text):
        # Remove duplicate instances of 'The candidate should be able to: '
        paragraph_text = paragraph_text.replace('The candidate should be able to: The candidate should be able to: ', 'The candidate should be able to: ')
 
        # Replace special characters with a numbered list
        special_chars = ['□']
        for char in special_chars:
            paragraph_text = paragraph_text.replace(char, '-')
 
        return paragraph_text
   
    def save_metadata_to_csv(self, csv_file):
        metadata_df = pd.DataFrame([m.dict() for m in self.metadata])
        metadata_df.to_csv(csv_file, index=False)
        print(f"Metadata saved to {csv_file}")
 
    def save_content_to_csv(self, csv_file):
        content_df = pd.DataFrame([c.dict() for c in self.content])
        content_df.to_csv(csv_file, index=False)
        print(f"Content data saved to {csv_file}")
 
    def save_to_csv(self, metadata_csv_file, content_csv_file):
        self.save_metadata_to_csv(metadata_csv_file)
        self.save_content_to_csv(content_csv_file)
 

def parse_xml(user_id):
    find_xml_files(xml_path)
    print('check files name:')
    for i, file in enumerate(METADATA_FILES):
        print(i, file)
    
    dataset = Dataset(user_id)
    if xml_path is not None:
        metadata_csv_file =  xml_path + '/metadata.csv'
        content_csv_file =  xml_path + '/content.csv'
        print('csv PATTTTTTH:' , metadata_csv_file, content_csv_file)
    else:
        print('error not file path in environment variable')
    dataset.save_to_csv(metadata_csv_file, content_csv_file)