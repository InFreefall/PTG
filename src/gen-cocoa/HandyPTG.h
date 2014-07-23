/**
 * Autogenerated by Thrift Compiler (0.7.0-dev)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 */

#import <Foundation/Foundation.h>

#import <TProtocol.h>
#import <TApplicationException.h>
#import <TProtocolUtil.h>
#import <TProcessor.h>


@interface HPTGEvent : NSObject <NSCoding> {
  int32_t __index;
  NSString * __type;
  int32_t __sender;
  NSArray * __data;
  NSString * __senderName;

  BOOL __index_isset;
  BOOL __type_isset;
  BOOL __sender_isset;
  BOOL __data_isset;
  BOOL __senderName_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, getter=index, setter=setIndex:) int32_t index;
@property (nonatomic, retain, getter=type, setter=setType:) NSString * type;
@property (nonatomic, getter=sender, setter=setSender:) int32_t sender;
@property (nonatomic, retain, getter=data, setter=setData:) NSArray * data;
@property (nonatomic, retain, getter=senderName, setter=setSenderName:) NSString * senderName;
#endif

- (id) initWithIndex: (int32_t) index type: (NSString *) type sender: (int32_t) sender data: (NSArray *) data senderName: (NSString *) senderName;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (int32_t) index;
- (void) setIndex: (int32_t) index;
- (BOOL) indexIsSet;

- (NSString *) type;
- (void) setType: (NSString *) type;
- (BOOL) typeIsSet;

- (int32_t) sender;
- (void) setSender: (int32_t) sender;
- (BOOL) senderIsSet;

- (NSArray *) data;
- (void) setData: (NSArray *) data;
- (BOOL) dataIsSet;

- (NSString *) senderName;
- (void) setSenderName: (NSString *) senderName;
- (BOOL) senderNameIsSet;

@end

@protocol HandyPTG <NSObject>
- (NSArray *) HPTGgetEvents: (int32_t) sinceIndex;  // throws TException
- (void) HPTGdrawCard;  // throws TException
- (void) HPTGplayCard: (NSString *) abbreviation : (NSString *) index;  // throws TException
- (void) HPTGlandCard: (NSString *) abbreviation : (NSString *) index;  // throws TException
- (void) HPTGdiscardCard: (NSString *) abbreviation : (NSString *) index;  // throws TException
- (NSString *) HPTGgetCard: (NSString *) abbreviation : (NSString *) index;  // throws TException
@end

@interface HandyPTGClient : NSObject <HandyPTG> {
  id <TProtocol> inProtocol;
  id <TProtocol> outProtocol;
}
- (id) initWithProtocol: (id <TProtocol>) protocol;
- (id) initWithInProtocol: (id <TProtocol>) inProtocol outProtocol: (id <TProtocol>) outProtocol;
@end

@interface HandyPTGProcessor : NSObject <TProcessor> {
  id <HandyPTG> mService;
  NSDictionary * mMethodMap;
}
- (id) initWithHandyPTG: (id <HandyPTG>) service;
- (id<HandyPTG>) service;
@end

@interface HandyPTGConstants : NSObject {
}
@end